# chatGPT_mock
chatGPTを検証するためのアプリケーション

openAIが提供しているAPI
* text completion: テキストの補完
* chat completion: 会話の補完(会話)
* image generation: 画像の生成


## chat completion
roleとしてsystemで入力することでより適切な解答が可能になる
また、userを先に入力しておき、アシスタントが答えることを入力することで、会話の方向性を絞ることができる
チャットの中で要約やコードの出力等も全部対応できる。
プロンプトが重要


## image generation
* テキストで入力した画像を生成する機能
* 編集機能
* 画像の種類を増やす機能


## 料金
$0.002 / 1K tokens
0.26円/ 1K tokens
0.00026円/一単語

tokensの計算は、入出力の何方も計算に入るので、注意が必要
節約には英語で入れることが重要
日本語 => 翻訳 => 英語　=> chatGPT => 英語 => 翻訳 => 日本語
使用料金制限も可能なので、設定する
