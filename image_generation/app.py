import openai
from dotenv import load_dotenv
import os
load_dotenv()

open_ai_api_key = os.getenv('OPEN_AI_API_KEY')
if not open_ai_api_key:
    exit()
openai.api_key = open_ai_api_key


response = openai.Image.create(
  prompt="白い猫",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)

