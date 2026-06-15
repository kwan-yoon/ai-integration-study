from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

# 멀티턴 대화 구현
history = []

def chat(user_input):
  # 사용자 메시지를 히스토리에 추가
  history.append({
    "role": "user",
    "parts": [{"text": user_input}]
  })

  # 전체 히스토리를 포함해서 API를 호출
  response = client.models.generate_content(
    model = "gemini-2.5-flash-lite",
    contents = history,
    config = types.GenerateContentConfig(
      system_instruction = "당신은 친절한 AI 어시스턴트입니다."
    )
  )

  ai_response = response.text

  # AI 응답도 히스토리에 추가
  history.append({
    "role": "model",
    "parts": [{"text": ai_response}]
  })

  return ai_response

# 멀티턴 대화 테스트
print(" 멀티턴 대화 테스트 \n")

questions = [
  "안녕 반가워, 내 이름은 K야",
  "내 이름이 뭔지 기억해?",
  "나는 AI 통합 개발을 학습하고 있어",
  "내가 뭘 배우고 있다고 했지?"
]

for q in questions:
  print(f"나 : {q}")
  response = chat(q)
  print(f"AI: {response}\n")


# 히스토리 확인
print(f" 총 대화 턴 수: {len(history) // 2}")