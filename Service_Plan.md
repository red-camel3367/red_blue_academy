# LLM Multi-Runner 프로젝트 기획서

## 📋 프로젝트 개요

### 프로젝트명

**LLM Multi-Runner** - 비용 효율적인 다중 LLM 동시 호출 및 벤치마킹 서비스

### 프로젝트 목표

최소 비용으로 5종 이상의 최신 LLM(Gemini, ChatGPT, Claude, Perplexity 등)에 동시 쿼리를 수행하고, 응답 품질과 속도, 비용을 비교하는 플랫폼 구축

### 개발 기간

**4주 (28일)**

### 지원 플랫폼

- **반응형 웹 (Desktop, Tablet, Mobile)**
- (추후 확장) 모바일 웹앱

---

## 🎯 핵심 기능

### 1. 다중 LLM 동시 실행 엔진

- **대상 모델**:
  - **Google**: Gemini 2.5 Flash (주력/무료 티어 활용)
  - **OpenAI**: GPT-4o Mini
  - **Anthropic**: Claude 3 Haiku
  - **Perplexity**: Sonar / Online
  - **Open Source**: Llama 3 (via Groq 등)
- **동작 방식**: `AsyncIO`를 활용한 비동기 병렬 호출로 대기 시간 최소화
- **비교 항목**: 응답 내용, 소요 시간(Latency), 소모 토큰 수, 추정 비용

### 2. 비용 최적화 시스템 (Smart Caching)

- **1차 캐싱**: Redis 기반 Key-Value 매칭으로 동일 쿼리 즉시 반환 (API 호출 0회)
- **2차 캐싱**: 시맨틱(의미) 검색을 통한 유사 질문 감지 및 답변 재사용
- **모델 라우팅**: 무료/저가 모델 우선 호출 및 사용자 설정에 따른 고비용 모델 제한 기능

### 3. 회원 맞춤형 아카이빙

- **쿼리 이력 저장**: 사용자가 수행한 질문과 5개 모델의 답변 영구 저장
- **개인화 대시보드**:
  - 일별/월별 사용량 통계
  - 선호하는 모델 분석 (좋아요/채택 기반)
- **내보내기**: 비교 결과를 Markdown 또는 PDF로 공유 가능

### 4. 실시간 모니터링 및 알림

- **비용 관리**: API 총비용이 설정된 일일 예산(예: 1,000원) 도달 시 서비스 제한 또는 관리자 알림
- **상태 점검**: 각 LLM API의 장애 여부 및 응답 속도 실시간 체크

---

## 🏗️ 기술 스택

### Frontend

- **프레임워크**: React (Next.js)
- **언어**: TypeScript
- **UI 라이브러리**: Tailwind CSS / Shadcn UI
- **상태관리**: Zustand or React Query

### Backend

- **런타임**: Python
- **프레임워크**: FastAPI (비동기 처리에 최적화)
- **데이터베이스**:
  - **NoSQL**: Google Firestore (사용자/로그 저장, 무료 등급 활용)
  - **Cache**: Redis (인메모리 캐싱)
- **인증**: Firebase Auth or OAuth 2.0

### AI/Infra

- **SDK**: LangChain / Official SDKs (OpenAI, Google GenAI, etc.)
- **클라우드**: Google Cloud Platform (GCP)
- **컴퓨팅**: Cloud Run (서버리스, 자동 확장)
- **배포/CI**: GitHub Actions

---

## 📅 4주 개발 일정

### 1주차 (환경 구축 및 프로토타입)

- **Day 1-2**: GCP 프로젝트 설정(Cloud Run, Firestore) 및 FastAPI 기본 골격 구성
- **Day 3-4**: 5개 LLM API 키 발급 및 기본 연동 테스트
- **Day 5-7**: 비동기 병렬 호출 로직 구현 및 단위 테스트

### 2주차 (핵심 기능 및 캐싱)

- **Day 8-10**: Redis 연동 및 쿼리 캐싱(Exact Match) 로직 개발
- **Day 11-12**: 회원가입/로그인(Auth) 및 DB 스키마 설계
- **Day 13-14**: 프론트엔드 기본 UI 개발 (쿼리 입력창, 결과 카드 뷰)

### 3주차 (서비스 고도화)

- **Day 15-17**: 시맨틱 캐싱 로직 도입 (Vector Search 검토)
- **Day 18-19**: 사용자 쿼리 히스토리 및 상세 조회 페이지 구현
- **Day 20-21**: 비용 모니터링 대시보드 및 예산 제한 기능 구현

### 4주차 (최적화 및 배포)

- **Day 22-24**: UI/UX 폴리싱 및 모바일 반응형 최적화
- **Day 25-26**: 통합 테스트, API 예외 처리(Rate Limit 대응) 강화
- **Day 27-28**: 운영 환경 배포 및 무료 등급 비용 한계 테스트

---

## 🎯 성공 지표 (KPI)

### 기술적 지표

- **캐시 적중률 (Cache Hit Rate)**: 30% 이상 (동일/유사 질문 방어)
- **평균 응답 속도**: 5초 이내 (모든 모델 응답 완료 기준)
- **API 호출 성공률**: 99% 이상 (Fallback 처리 포함)

### 비즈니스 지표

- **운영 비용**: 월 $5 미만 유지 (GCP 무료 티어 + Gemini Flash 활용)

---

## ⚠️ 리스크 및 대응방안

### 기술적 리스크

1. **API Rate Limit (사용량 제한)**

   - 대응: Round Robin 방식의 키 교체 또는 대기 큐(Queue) 시스템 도입
   - 대응: 사용량 초과 시 '잠시 후 다시 시도해주세요' UX 제공

2. **응답 형식 불일치**
   - 대응: 모든 LLM 응답을 표준화된 JSON 포맷으로 파싱하는 전처리 모듈 강화

### 비즈니스 리스크

1. **API 정책 및 가격 변동**
   - 대응: 주기적인 가격 모니터링 및 저렴한 대체 모델(Open Source 등) 즉시 교체 가능하도록 모듈화 설계
