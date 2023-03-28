import openai
from dotenv import load_dotenv
import os
load_dotenv()

open_ai_api_key = os.getenv('OPEN_AI_API_KEY')
if not open_ai_api_key:
    exit()
openai.api_key = open_ai_api_key


def chat_with_gpt(text):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "system", "content": "あなたは学校の先生です。"},
                {"role": "user", "content": f"{text}"}],
    )
    message = response.choices[0].message.content
    return message


prompt = "今日の天気はどうなると思いますか？"
response_text = chat_with_gpt(prompt)
print(response_text)
