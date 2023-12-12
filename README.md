# Image Generation and Resizing Script
- This Python script is designed with AWS Lambda in mind.

## image_generate.py
- Generates images using DALL-E.
- The output is the URL of the generated image.
- An OpenAI API key is required.

```
$ pip3 install openai

# python3 ./image_generate.py model prompt width height
$ python3 ./image_generate.py "dall-e-2" "a girl, stencil art" "256" "256"
$ python3 ./image_generate.py "dall-e-3" "a girl, stencil art" "256" "256"
```

## image_resize.py
- Resizes a given image.
- The Pillow library is required.
- Resizes while maintaining the aspect ratio.
    - This process involves creating a background with the size of the resized image and pasting the aspect ratio-adjusted image onto it.

```
$ pip3 install Pillow

# python3 ./image_resize.py input_path output_path width height
$ python3 ./image_resize.py "./${generated_file_name}" "./${resized_file_name}" "1164" "498"
```

## image_resolution.py
- Automatically adjusts the resolution of a given image.
- Currently, many values are preset, so fine adjustments are not possible.

```
$ pip3 install Pillow
$ pip3 install diffusers
$ pip3 install torch
$ pip3 install transformers
$ pip3 install accelerate

# python3 ./image_resolution.py input_path output_path
$ python3 ./image_resolution.py "./${generated_file_name}" "./${resized_file_name}"
```

(Note: This translation covers the full content as per the snippet shown. If there is additional content, please let me know to continue the translation.)

## prompt_translate.py
- Translates text passed as an argument into any language.
- The source and target languages are assumed to be written in English.

```
$ pip3 install openai
$ python3 ./prompt_translate.py "Welcome to the colorful and cute world of Toon Cats! A special piece for cat lovers. What's depicted here is a Toon Cat with vivid colors and a playful expression, as if it's jumped right out of an animation. This cat is not just a character. It's the protagonist of an adventure-filled story, always bringing a smile to our faces, a lovely presence." "Japanese" "English"
```

## sample.sh
A sample script that combines existing Python scripts to generate an image from a prompt and then resize it.
