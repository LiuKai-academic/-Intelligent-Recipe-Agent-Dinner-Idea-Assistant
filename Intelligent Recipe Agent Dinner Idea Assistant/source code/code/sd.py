import requests
import os
import base64
from PIL import Image
from io import BytesIO
import uuid

def generate_image(recipe):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    body = {
        "steps": 40,
        "width": 1024,
        "height": 1024,
        "seed": 0,
        "cfg_scale": 5,
        "samples": 1,
        "text_prompts": [
            {
                "text": f"A plate of {recipe}, vibrant colors, high detail, served on a white ceramic plate, garnished with green herbs, shot in a well-lit kitchen setting, (best quality,4k,8k,highres,masterpiece:1.2), ultra-detailed, (realistic,photorealistic,photo-realistic:1.37), HDR, UHD, studio lighting, ultra-fine painting, sharp focus, traditional Chinese cuisine style, warm and inviting tones, natural lighting.",
                "weight": 1
            },
            {
                "text": "nsfw, (low quality,normal quality,worst quality,jpeg artifacts), cropped, monochrome, lowres, low saturation, ((watermark)), (white letters), food stains, unappetizing, overcooked, undercooked, burnt, poorly arranged, out of focus, blurred, dirty plate, unclean background, unappealing presentation.",
                "weight": -1
            }
        ]
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "sk-dVfdqL7vvWzAf3oDqmToFXzOaHOPhDjSOh5cdxg2BUrZ9Ay0",
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    if not os.path.exists("./out"):
        os.makedirs("./out")

    image_path = ''
    for i, image in enumerate(data["artifacts"]):
        image_data = base64.b64decode(image["base64"])
        img = Image.open(BytesIO(image_data))
        
        # Resize the image to 1/4 of the original size
        new_size = (img.width // 4, img.height // 4)
        resized_image = img.resize(new_size, Image.LANCZOS)
        
        unique_id = uuid.uuid4()  # Generate a unique identifier
        
        image_path = f'./out/txt2img_{i}_{unique_id}.png'
        resized_image.save(image_path)

    return image_path
