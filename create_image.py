## Generates images with dalle

# https://platform.openai.com/docs/quickstart

# API: https://platform.openai.com/docs/api-reference/images/create

# Call with `python .\create_image.py "this is my prompt"`

import os
from openai import OpenAI
import requests
import sys


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
content = img_data.content
img_name = prompt

if not os.path.exists("output"):
    os.makedirs("output")

with open(f"output/{img_name}.png", "wb") as handler:
    handler.write(content)
