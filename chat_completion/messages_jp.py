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
      messages=[
          {"role": "system", "content": "あなたは学校の先生です、今日の天気は晴れです。"},
          # {"role": "user", "content": "今日の天気はどうなると思いますか？"},
          # {"role": "assistant", "content": "申し訳ありません、私は天気予報に関する情報を持っていません。"
          #                                  "ただし、インターネットやスマートフォンの天気アプリを使用すると、正確な天気予報を取得できます。"
          #                                  "学校の生徒たちが出かける予定のある場合は、天気が荒れている場合には注意が必要ですので、事前に確認することをお勧めします。"},
          {"role": "user", "content": f"{text}"}
      ],
    )
    message = response.choices[0].message.content
    return message


prompt = """次の文を要約して「every day, every night
君を想ってばかりで
どうにかなりそうなんだ

ほんの少しの
ためらいに立ち止まって
愛の痛みを知ったよ

今、時を止めるのさ
僕にしかできない事がある

花束のかわりにメロディーを
抱きしめるかわりにこの声を
いつも遠くから 君を見ていた
でも今日は僕を見つめて

たった一人
守るだけの強さが
僕にもあるとするなら

Ohh Baby 君を
君だけは守りたい
この手を握ってくれる君

君を愛する為に
僕は生まれてきたよ

花束のかわりにメロディーを
抱きしめるかわりにこの声を
僕じゃなきゃ駄目で 君じゃなきゃ駄目さ
だから今は僕を見つめて

もう誰にも、僕を語らせはしない
君がいれば 他に何もいらない
i love you

君に愛される為に
僕は生まれてきたよ

花束のかわりにメロディーを
抱きしめるかわりにこの声を
いつも遠くから 君を見ていた
でも今日は僕を見つめて

僕じゃなきゃ駄目で 君じゃなきゃ駄目さ
だから今は僕を見つめて

今夜だけは僕を見つめて」"""
response_text = chat_with_gpt(prompt)
print(response_text)
