# 画像生成、および、リサイズ用スクリプト
- pythonスクリプトは、AWS Lambdaを意識した作りにしてみました。

## image_generate.py
- DALL-Eを使用して、画像生成します。
- 出力は生成した画像のURLです。
- OpenAIのAPIキーが必須です。

```
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



## sample.sh
image_generate.pyとimage_resize.pyを組み合わせて、
画像生成→画像リサイズを行うサンプルスクリプトです。

