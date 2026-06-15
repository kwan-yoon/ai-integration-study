from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

# JSON 형식으로 응답 받기
response = client.models.generate_content(
  model = "gemini-2.5-flash-lite",
  contents = "사과, 바나나, 포도의 칼로리 알려줘",
  config = types.GenerateContentConfig(
    system_instruction = """
      반드시 아래 JSON 형식으로만 답하세요. 다른 텍스트는 포함하지 마세요.
      {
        "fruits": [
          {"name": "과일이름", "calories_per_100g": 숫자}
        ]
      }
    """
  )
)

print("원본 응답")
raw = response.text
print(raw)


# JSON 파싱
print("\n JSON 파싱")
try:
  # 코드블록 제거 (```json ... ``` 형태로 올 수 있음)
  cleaned = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
  data = json.loads(cleaned)

  for fruit in data["fruits"]:
    print(f"{fruit['name']}: {fruit['calories_per_100g']}kcal/100g")

except json.JSONDecodeError as e:
  print(f"파싱 실패: {e}")


# 에러 핸들링
print("\n 에러 핸들링")

try:
  response = client.models.generate_content(
    model = "gemini-2.5-flash-lite",
    contents = "오늘 날씨 어때?",
    config = types.GenerateContentConfig(
      max_output_tokens = 5
    )
  )

  data = json.loads(response.text)
  print(data)

except json.JSONDecodeError:
  print("JSON 파싱 실패 - 응답이 JSON 형식이 아닙니다.")
except Exception as e:
  print(f"기타 에러: {e}")