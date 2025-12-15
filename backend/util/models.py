import os
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

# 1. 모델 정의
def get_models():
    return {
        "gemini": ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.7,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        ),
        "gpt4o_mini": ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.7,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        ),
        "claude_haiku": ChatAnthropic(
            model="claude-3-haiku-20240307",
            temperature=0.7,
            anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
        ),
        # Perplexity는 OpenAI 호환 인터페이스 사용
        "perplexity": ChatOpenAI(
            model="llama-3-sonar-small-32k-online",
            openai_api_key=os.getenv("PERPLEXITY_API_KEY"),
            base_url="https://api.perplexity.ai"
        ),
        # Groq (Llama 3)도 OpenAI 호환 인터페이스 사용
        "llama3_groq": ChatOpenAI(
            model="llama3-8b-8192",
            openai_api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )
    }

# 2. 비용 테이블 (1M 토큰 당 USD) - 기획서 기반 추정치
PRICE_TABLE = {
    "gemini": {"input": 0.00, "output": 0.00}, # 무료 티어 가정
    "gpt4o_mini": {"input": 0.15, "output": 0.60},
    "claude_haiku": {"input": 0.25, "output": 1.25},
    "perplexity": {"input": 0.20, "output": 0.20}, # 예시
    "llama3_groq": {"input": 0.05, "output": 0.10}  # 예시
}