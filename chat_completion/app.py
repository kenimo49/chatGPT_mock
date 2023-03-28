import openai
from dotenv import load_dotenv
import os
load_dotenv()

open_ai_api_key = os.getenv('OPEN_AI_API_KEY')
if not open_ai_api_key:
    exit()
openai.api_key = open_ai_api_key


def chat_with_gpt():
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )
    message = response.choices[0].message
    return message


response_text = chat_with_gpt()
print(response_text)
