import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# API 키 가져오기 (없으면 에러 발생 혹은 None)
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")