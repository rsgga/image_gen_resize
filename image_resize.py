import sys
import json
from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    with Image.open(input_path) as img:
        img = img.resize((new_width, new_height))
        img.save(output_path)

def lambda_handler(event, context):
    body = json.loads(event['body'])

    input_path  = body['input']
    output_path = body['output']
    new_width   = int(body['width'])
    new_height  = int(body['height'])

    resize_image(input_path, output_path, new_width, new_height)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python resize_image.py <input_path> <output_path> <new_width> <new_height>")
        sys.exit(1)

    input_path  = sys.argv[1]
    output_path = sys.argv[2]
    new_width   = int(sys.argv[3])
    new_height  = int(sys.argv[4])

    json_body = json.dumps({
        "input":  input_path,
        "output": output_path,
        "width":  new_width,
        "height": new_height
    })

    lambda_handler({ "body": json_body }, {})

