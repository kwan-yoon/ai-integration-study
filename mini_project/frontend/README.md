# AI Integration Study

Gemini API를 활용한 AI 통합 학습 레포지토리입니다.
Python 기초부터 풀스택 AI 웹앱 개발까지 단계별로 학습한 내용을 담고 있습니다.

---

## 🗺️ 학습 로드맵

| 단계  | 내용                                     | 상태    |
| ----- | ---------------------------------------- | ------- |
| 0단계 | Python 문법 기초                         | ✅ 완료 |
| 1단계 | Gemini API 기초 + 풀스택 미니 프로젝트   | ✅ 완료 |
| 2단계 | LangChain + RAG 실전 프로젝트            | 🔜 예정 |
| 3단계 | 서비스 운영 관점 (비용 최적화, 모니터링) | 🔜 예정 |

---

## 0단계 — Python 문법

AI 개발에 필요한 Python 기초 문법을 학습했습니다.

### 학습 내용

- 변수, 자료형, 조건문, 반복문
- 함수, 클래스, 모듈
- 파일 입출력, 예외 처리
- 라이브러리 활용 (pip, venv)

---

## 1단계 — Gemini API 기초

Google Gemini API를 활용한 AI 통합 학습을 진행했습니다.

### Day별 학습 내용

| 파일                      | 내용                       |
| ------------------------- | -------------------------- |
| day01_first_call.py       | Gemini API 첫 호출         |
| day02_api_structure.py    | API 구조 및 요청/응답 이해 |
| day03_prompt_design.py    | 프롬프트 설계 기법         |
| day04_response_parsing.py | 응답 파싱 및 데이터 처리   |
| day05_multi_turn.py       | 멀티턴 대화 구현           |

---

## 1단계 미니 프로젝트 — AI 챗봇 웹앱

Gemini API를 백엔드에 연결한 풀스택 AI 챗봇 웹앱입니다.
채팅 기능과 텍스트 요약 기능을 제공합니다.

### 기술 스택

**Backend**

- Python 3.14
- FastAPI
- google-genai (Gemini 2.5 Flash)
- python-dotenv
- uvicorn

**Frontend**

- React
- TypeScript
- Tailwind CSS
- Vite
- Axios

### 주요 기능

- 💬 AI와 실시간 채팅
- 📝 텍스트 3줄 요약

### 프로젝트 구조

```
mini_project/
├── backend/
│   ├── main.py          # FastAPI 서버 + Gemini API 연결
│   ├── .env             # API 키 (git 제외)
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── api/
    │   │   └── client.ts        # 백엔드 API 호출 함수
    │   ├── components/
    │   │   ├── ChatWindow.tsx   # 채팅 UI 컴포넌트
    │   │   └── SummaryPanel.tsx # 텍스트 요약 UI 컴포넌트
    │   └── App.tsx              # 전체 레이아웃 + 탭 전환
    └── ...
```

### API 엔드포인트

| Method | Endpoint   | 설명           |
| ------ | ---------- | -------------- |
| GET    | /health    | 서버 상태 확인 |
| POST   | /chat      | AI 채팅        |
| POST   | /summarize | 텍스트 요약    |

### 실행 방법

**Backend**

```bash
cd mini_project/backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend**

```bash
cd mini_project/frontend
npm install
npm run dev
```

### 환경 변수 설정

`mini_project/backend/.env` 파일 생성 후 아래 내용 추가:

```
GEMINI_API_KEY=your_api_key_here
```
