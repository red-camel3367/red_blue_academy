import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# API 키 가져오기 (없으면 에러 발생 혹은 None)
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# 검색 쿼리 설정
SEARCH_QUERY = "보험 산업 규제 및 시장 동향"

# 도메인 리스트 (news_domain.py의 내용을 여기로 이동)
KOREAN_NEWS_DOMAINS = [
    # 1. 보험/금융 전문지 (기존 유지 + 추가)
    "insnews.co.kr",        # 한국보험신문
    "fins.co.kr",           # 보험저널
    "kbanker.co.kr",        # 대한금융신문
    "fntimes.com",          # 한국금융신문
    "joseilbo.com",         # 조세일보 (금융/보험 섹션 강함)
    "biz.newdaily.co.kr",   # 뉴데일리경제
    "inthenews.co.kr",      # 인더뉴스 (보험 섹션 특화)
    "consumernews.co.kr",   # 소비자가 만드는 신문 (보험 민원/이슈 관련)
    
    # 2. 메이저 경제지 (보험 기사 비중 매우 높음)
    "hankyung.com",         # 한국경제
    "mk.co.kr",             # 매일경제
    "sedaily.com",          # 서울경제
    "mt.co.kr",             # 머니투데이
    "fnnews.com",           # 파이낸셜뉴스
    "asiae.co.kr",          # 아시아경제
    "edaily.co.kr",         # 이데일리
    "heraldbiz.com",        # 헤럴드경제
    "etoday.co.kr",         # 이투데이
    "biz.chosun.com",       # 조선비즈
    "bizwatch.co.kr",       # 비즈워치 (기업 공시/분석 강점)
    "dt.co.kr",             # 디지털타임스
    
    # 3. 주요 통신사 (속보/팩트 위주)
    "yna.co.kr",            # 연합뉴스
    "news1.kr",             # 뉴스1
    "newsis.com",           # 뉴시스
    
    # 4. 종합 일간지 (사회적 파급력 있는 보험 이슈)
    "chosun.com",           # 조선일보
    "joongang.co.kr",       # 중앙일보
    "donga.com",            # 동아일보
    "hani.co.kr",           # 한겨레
    "khan.co.kr",           # 경향신문
    "kmib.co.kr",           # 국민일보
    "segye.com",            # 세계일보
    "munhwa.com",           # 문화일보
    "daily.hankooki.com",   # 한국일보
    
    # 5. 방송사 뉴스 (대형 사건/사고 보도)
    "news.kbs.co.kr",       # KBS 뉴스
    "imnews.imbc.com",      # MBC 뉴스
    "news.sbs.co.kr",       # SBS 뉴스
    "ytn.co.kr",            # YTN
    "yonhapnewstv.co.kr",   # 연합뉴스TV
    
    # 6. IT/테크 (인슈어테크, AI, 핀테크 관련)
    "etnews.com",           # 전자신문
    "zdnet.co.kr",          # ZDNet Korea
    "ddaily.co.kr",         # 디지털데일리
    "bloter.net",           # 블로터
    "byline.network",       # 바이라인네트워크 (테크 심층)
    "irobotnews.com",       # 로봇/AI 관련
    
    # 7. 기타 경제/산업 매체
    "dailian.co.kr",        # 데일리안
    "nocutnews.co.kr",      # 노컷뉴스
    "pressian.com",         # 프레시안
    "thebell.co.kr",        # 더벨 (자본시장/M&A 심층)
    "ceo.co.kr"             # CEO스코어데일리
]