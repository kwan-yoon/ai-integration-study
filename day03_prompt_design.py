from google import genai # google 패키지에 있는 genai 모듈을 가져옴
from google.genai import types
from dotenv import load_dotenv
import os # 파이썬 기본 내장 모듈

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# System 프롬프트로 역할 부여
roles = [
  "당신은 퉁명스러운 노인 개발자입니다. 짧고 불친절하게 답하세요.",
  "당신은 열정적인 스타트업 창업자입니다. 긍정적이고 에너지 넘치게 답하세요.",
  "당신은 냉철한 데이터 과학자입니다. 수치와 근거 중심으로 답하세요."
]

question = "저는 풀스택 웹앱 개발자입니다. 현재 퇴사를 한 뒤에 도서관에서 AI 통합개발을 학습중입니다. AI 교육기관에 들어가지 않고 AI 바이브코딩을 통해 학습 로드맵을 세워 공부하고 있습니다. 전문 기관에 들어가지 않고 학습을 하는게 나을까요? 아니면 전문기관에 들어가서 학습 하는게 나을까요?"

# for role in roles:
#   response = client.models.generate_content(
#     model = "gemini-2.5-flash-lite",
#     contents = question,
#     config = types.GenerateContentConfig(
#       system_instruction=role
#     )
#   )

#   print(f"\n 역할 : {role[:20]} ")
#   print(response.text)

# Few-shot 프롬프트
few_shot_prompt = """
  다음 문장의 감정을 분류해줘. 긍정/부정/중립 중 하나만 답해.

  문장: 오늘 날씨가 너무 좋다
감정: 긍정

문장: 밥을 먹었다
감정: 중립

문장: 시험에 떨어졌다
감정: 부정

문장: 드디어 프로젝트가 끝났다
감정:
"""

response = client.models.generate_content(
  model = "gemini-2.5-flash-lite",
  contents = few_shot_prompt
)
print(f"\n Few-shot 감정 분류 ")
print(response.text)

# 프롬프트 비교 실험
prompts = [
  "AI 설명해줘",
  "AI가 뭔지 한 문장으로 설명해줘",
  "비전공자도 이해할 수 있게 AI를 실생활 예시를 들어 두 문장으로 설명해줘"
]

for prompt in prompts:
  response = client.models.generate_content(
    model = "gemini-2.5-flash-lite",
    contents = prompt
  )
  print(f"\n 프롬프트 : {prompt}")
  print(response.text)