from google import genai # 공식 문서 및 모든 예제에서 쓰는 관례 genai
from dotenv import load_dotenv
import os

# .env 파일에서 API 키 로드
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 클라이언트 설정
client = genai.Client(api_key = api_key)

# 첫 번째 호출
response = client.models.generate_content(
  model = 'gemini-2.5-flash-lite',
  contents = '안녕하세요! 당신은 누구인가요?'
)

# 응답 출력
print(response.text)