from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 1. role 구조 실험 (system / user)
response = client.models.generate_content(
  model = "gemini-2.5-flash-lite",
  contents = "파이썬이 뭐야?",
  config = types.GenerateContentConfig(
    system_instruction = "당신은 5살 아이에게 설명하는 선생님입니다. 아주 쉽고 짧게 답하세요."
  )
)

print("System 역할 실험")
print(response.text)

# 2. temperature 실험
for temp in [0.0, 1.0, 2.0]:
  response = client.models.generate_content(
    model = "gemini-2.5-flash-lite",
    contents = "오늘 기분을 한 문장으로 표현해줘",
    config = types.GenerateContentConfig(
      temperature = temp
    )
  )

  print(f"\n Temperature {temp}")
  print(response.text)

# 3. max_tokens 실험
for tokens in [10, 50, 200]:
  response = client.models.generate_content(
    model = "gemini-2.5-flash-lite",
    contents = "인공지능이란 무엇인가요?",
    config = types.GenerateContentConfig(
      max_output_tokens=tokens
    )
  )

  print(f"\n max_tokens {tokens}")
  print(response.text)