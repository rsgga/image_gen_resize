import sys
import json
from PIL import Image
from io import BytesIO
from diffusers import StableDiffusionUpscalePipeline
import torch

STABLE_DIFFUSION_MODEL_ID = "stabilityai/stable-diffusion-x4-upscaler"

#STABLE_DIFFUSION_PROMPT   = "photo realistic, normal quality, masterpiece, an extremely delicate and beautiful, extremely detailed"

def model_id():
    return STABLE_DIFFUSION_MODEL_ID

def prompt():
    return STABLE_DIFFUSION_PROMPT

def image(input_path):
    low_res_img = Image.open(input_path).convert("RGB")

    return low_res_img

def gen_pipeline(device, torch_dtype):
    pipeline = StableDiffusionUpscalePipeline.from_pretrained(model_id(), torch_dtype=torch_dtype)
    pipeline = pipeline.to(device)

    return pipeline

def cpu_pipeline():
    return gen_pipeline("cpu", torch.float)


def cuda_pipeline():
    return gen_pipeline("cuda", torch.float16)

def torch_dtype(device):
    return {
        "cpu":  torch.float,
        "cuda": torch.float16
    }[device]

# Only "cuda" or "cpu"
def device_type():
    return "cuda" if torch.cuda.is_available() else "cpu"

def resolution_image(input_path, output_path, prompt):
    device = device_type()
    pipeline = gen_pipeline(device, torch_dtype(device))

    upscaled_image = pipeline(prompt=prompt, image=image(input_path)).images[0]
    upscaled_image.save(output_path)

def lambda_handler(event, context):
    body = json.loads(event['body'])

    input_path  = body['input']
    output_path = body['output']
    prompt      = body['prompt']

    resolution_image(input_path, output_path, prompt)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python resolution_image.py <input_path> <output_path> <prompt>")
        sys.exit(1)

    input_path  = sys.argv[1]
    output_path = sys.argv[2]
    prompt      = sys.argv[3]

    json_body = json.dumps({
        "input":  input_path,
        "output": output_path,
        "prompt": prompt
    })

    lambda_handler({ "body": json_body }, {})

