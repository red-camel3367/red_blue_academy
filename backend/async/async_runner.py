import time
import asyncio
from langchain_core.messages import HumanMessage
from ..util.models import get_models, PRICE_TABLE

class LLMRunner:
    def __init__(self):
        self.models = get_models()

    def calculate_cost(self, model_name, input_tokens, output_tokens):
        prices = PRICE_TABLE.get(model_name, {"input": 0, "output": 0})
        cost = (input_tokens * prices["input"] / 1_000_000) + \
               (output_tokens * prices["output"] / 1_000_000)
        return round(cost, 6)

    async def _invoke_single_model(self, name: str, model, query: str):
        start_time = time.time()
        status = "success"
        response_content = ""
        input_tokens = 0
        output_tokens = 0
        error_msg = None

        try:
            # LangChain 비동기 호출
            response = await model.ainvoke([HumanMessage(content=query)])
            
            response_content = response.content
            
            # 토큰 정보 추출 (모델마다 메타데이터 위치가 다를 수 있음. 표준화 필요)
            usage_metadata = response.response_metadata.get("token_usage", {})
            # OpenAI/Groq/Perplexity 등은 보통 'token_usage' 키를 사용
            if not usage_metadata:
                 # Anthropic 등 다른 구조일 경우 처리 로직 추가 필요 (여기선 간소화)
                 usage_metadata = response.response_metadata.get("usage", {})

            input_tokens = usage_metadata.get("prompt_tokens", 0)
            output_tokens = usage_metadata.get("completion_tokens", 0)

        except Exception as e:
            status = "error"
            error_msg = str(e)
            print(f"Error in {name}: {e}")

        latency = round(time.time() - start_time, 2)
        estimated_cost = self.calculate_cost(name, input_tokens, output_tokens)

        return {
            "model": name,
            "status": status,
            "content": response_content,
            "latency": latency,
            "tokens": {"input": input_tokens, "output": output_tokens},
            "cost_usd": estimated_cost,
            "error": error_msg
        }

    async def run_all(self, query: str):
        # 5개 모델 동시 실행 작업 생성
        tasks = [
            self._invoke_single_model(name, model, query)
            for name, model in self.models.items()
        ]
        # 병렬 실행 및 결과 대기
        results = await asyncio.gather(*tasks)
        return results