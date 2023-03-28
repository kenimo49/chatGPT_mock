import openai
from dotenv import load_dotenv
import os
load_dotenv()

open_ai_api_key = os.getenv('OPEN_AI_API_KEY')
if not open_ai_api_key:
    exit()
openai.api_key = open_ai_api_key

# フラミンゴがいるプールのある太陽に照らされた屋内ラウンジエリア
response = openai.Image.create_edit(
  image=open("sunlit_lounge.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)

