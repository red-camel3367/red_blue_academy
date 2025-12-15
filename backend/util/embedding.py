from langchain_core.globals import set_llm_cache
from langchain_community.cache import RedisSemanticCache
from langchain_community.embeddings import HuggingFaceEmbeddings

# 비용 0원인 로컬 임베딩 모델 사용
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

set_llm_cache(
    RedisSemanticCache(
        redis_url="redis://localhost:6379",
        embedding=embeddings,
        score_threshold=0.9 # 유사도 90% 이상이면 캐시 사용
    )
)