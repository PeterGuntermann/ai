## Generates images with dalle

# https://platform.openai.com/docs/quickstart

# API: https://platform.openai.com/docs/api-reference/images/create

# Call with `python .\create_image.py "this is my prompt"`

import os
from openai import OpenAI
import requests
import sys
from datetime import datetime


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


_, prompt = sys.argv

apikey = os.environ.get("OPENAI_API_KEY")

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

url = response.data[0].url
revised_prompt = response.data[0].revised_prompt

# Download
print(revised_prompt)
print(url)

# Download
img_data = requests.get(url)
img_name = prompt

timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
folder = f"output/{timestamp}-generated-image"
create_folder(folder)

with open(f"{folder}/{img_name}.png", "wb") as handler:
    handler.write(img_data.content)

with open(f"{folder}/prompt.txt", "w") as handler:
    handler.write("URL:\n")
    handler.write(url)
    handler.write("\n\n")
    handler.write("REVISED PROMPT:\n")
    handler.write(revised_prompt)
