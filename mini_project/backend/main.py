from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# CORS 설정 (React 프론트엔드 연결용)
app.add_middleware(
  CORSMiddleware,
  allow_origins = ['http://localhost:5173'],
  allow_methods = ["*"],
  allow_headers = ["*"]
)

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

# 요청 데이터 형식
class ChatRequest(BaseModel):
  message: str
  history: list = []

class SummaryRequest(BaseModel):
  text: str

# 채팅 엔드포인트
@app.post('/chat')
async def chat(req: ChatRequest):
  response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = req.message
  )
  return {"reply": response.text}

# 요약 엔드포인트
@app.post("/summarize")
async def summarize(req: SummaryRequest):
  prompt = f"다음 텍스트를 3줄로 요약해줘:\n\n{req.text}"
  response = client.models.generate_content(
    model = 'gemini-2.5-flash',
    contents = prompt
  )
  return {"summary": response.text}

@app.get('/health')
async def health():
  return {"status": "ok"}