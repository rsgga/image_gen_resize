import sys
import json
from openai import OpenAI

def generate_size_str(width, height):
    return f'{width}x{height}'

def allow_size():
    return {
        "dall-e-3": ["1024x1024", "1024x1792"],
        "dall-e-2": ["256x256", "512x512", "1024x1024"]
    }

def validate_model_and_size(model, size):
    # 利用可能なモデルとサイズの辞書
    available_options = allow_size()

    # モデルが辞書に存在するかチェック
    if model not in available_options:
        raise ValueError(f"Model '{model}' is not available.")

    # サイズがモデルの利用可能なサイズに含まれているかチェック
    if size not in available_options[model]:
        raise ValueError(f"Size '{size}' is not available for model '{model}'.")


def lambda_handler(event, context):
    client = OpenAI()

    body = json.loads(event['body'])

    _width   = body['width']
    _height  = body['height']

    model   = body['model']
    prompt  = body['prompt']
    size    = generate_size_str(_width, _height)
    quality = body['quality']

    response = client.images.generate(
      model=model,
      prompt=prompt,
      size=size,
      quality=quality,
      n=1,
    )

    image_url = response.data[0].url
    print(image_url)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python image_generate.py <model> <prompt> <width> <height>")
        sys.exit(1)

    model  = sys.argv[1]
    prompt = sys.argv[2]
    width  = int(sys.argv[3])
    height = int(sys.argv[4])

    # Fixed value
    quality = "standard"

    validate_model_and_size(model, generate_size_str(width, height))

    json_body = json.dumps({
        "model":   model,
        "prompt":  prompt,
        "width":   width,
        "height":  height,
        "quality": quality,
    })

    lambda_handler({ "body": json_body }, {})

