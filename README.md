# 画像生成、および、リサイズ用スクリプト
- pythonスクリプトは、AWS Lambdaを意識した作りにしてみました。

## image_generate.py
- DALL-Eを使用して、画像生成します。
- 出力は生成した画像のURLです。
- OpenAIのAPIキーが必須です。

```
$ pip3 install openai

# python3 ./image_generate.py  model prompt width height
$ python3 ./image_generate.py "dall-e-2" "a girl, stencil art" "256" "256"
$ python3 ./image_generate.py "dall-e-3" "a girl, stencil art" "256" "256"
```

## image_resize.py
- 与えられたイメージ画像をリサイズします。
- Pillowライブラリが必須です。
- アスペクト比を保持した上でリサイズします。
    - リサイズ後のサイズを持つ背景を生成して、そこにアスペクト比に応じてサイズ調整した画像を貼るような処理です。

```
$ pip3 install Pillow

# python3 ./image_resize.py input_path output_path  width height
$ python3 ./image_resize.py "./${generated_file_name}" "./${resized_file_name}" "1164" "498"
```

## imgae_resolution.py
- 与えられた画像の解像度を自動調整します
- 現状、決め内の値が多いので、細かい調整はできません。

```
$ pip3 install Pillow
$ pip3 install diffusers
$ pip3 install torch
$ pip3 install transformers
$ pip3 install accelerate

# python3 ./image_resolution.py input_path output_path
$ python3 ./image_resolution.py "./${generated_file_name}" "./${resized_file_name}"
```

## prompt_translate.py
- 引数として渡されたテキストを、任意の言語に翻訳します。
- 翻訳元と翻訳先の言語は、英語で記述することを想定しています。

```
$ pip3 install openai
$ python3 ./prompt_translate.py "『カラフルでキュートなトゥーン猫の世界へようこそ！』 猫好きのための特別な一枚 ここに描かれているのは、まるでアニメから飛び出してきたかのような、鮮やかな色彩と楽しい表情を持つトゥーン猫。この猫はただのキャラクターではありません。それは、冒険心溢れる物語の主人公、いつも私たちを笑顔にしてくれる、愛らしい存在です。" "Japanese" "English"
```

## sample.sh
存在するpythonスクリプトを組み合わせて、
プロンプトから画像生成→画像リサイズを行うためのサンプルスクリプトです。
