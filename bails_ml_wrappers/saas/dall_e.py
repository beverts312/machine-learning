import logging
import os

import openai
import requests

openai.api_key = os.getenv("OPENAI_API_KEY")


def download_result(url, name):
    req = requests.get(url, stream=True)
    with open(name, "wb") as f:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def generate_image(prompt, output_dir="output", count=4, size="1024x1024"):
    logging.info(f"Begin Generation: {prompt}")
    res = openai.Image.create(
        prompt=prompt,
        n=int(count),
        size=size,
    )
    logging.info("Generation Complete")
    for idx, img in enumerate(res["data"]):
        img_path = f"{output_dir}/{prompt.replace(' ', '_')}_{idx}.png"
        download_result(img["url"], img_path)
