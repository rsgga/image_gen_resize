import sys
import json
from PIL import Image

def get_resample_filter():
    return Image.LANCZOS

def calc_keep_aspect_new_size(original_size, output_size):
    original_width, original_height = original_size
    target_width,   target_height   = output_size

    ratio = min(target_width/original_width, target_height/original_height)

    return (int(original_width * ratio), int(original_height * ratio))

def resize_image_keep_aspect_ratio(img, output_size, resample_filter):
    new_size = calc_keep_aspect_new_size(img.size, output_size)
    img = img.resize(new_size, resample_filter)

    return img

# for centering
def top_left_point(img_size, canvas_size):
    img_width, img_height = img_size

    x = (canvas_size[0] - img_width) // 2
    y = (canvas_size[1] - img_height) // 2

    return (x, y)

def center_image_on_canvas(img, canvas_size):
    new_img = Image.new("RGB", canvas_size)

    new_img.paste(
        img,
        top_left_point(img.size, canvas_size)
    )

    return new_img

#def resize_image(input_path, output_path, output_size):
def resize_image(input_path, output_path, new_width, new_height):
    output_size = (new_width, new_height)

    with Image.open(input_path) as img:
        resample_filter = get_resample_filter()
        resized_img = resize_image_keep_aspect_ratio(img, output_size, resample_filter)

        adjusted_img = center_image_on_canvas(resized_img, output_size)
        adjusted_img.save(output_path)

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

