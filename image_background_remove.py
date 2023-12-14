import sys
import json
from rembg import remove

def remove_image_background(input_path, output_path):
    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            origin_img = i.read()
            removed_background_img = remove(origin_img)
            o.write(removed_background_img)

def lambda_handler(event, context):
    body = json.loads(event['body'])

    input_path  = body['input']
    output_path = body['output']

    remove_image_background(input_path, output_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python image_background_remove.py <input_path> <output_path>")
        sys.exit(1)

    input_path  = sys.argv[1]
    output_path = sys.argv[2]

    json_body = json.dumps({
        "input":  input_path,
        "output": output_path
    })

    lambda_handler({ "body": json_body }, {})

