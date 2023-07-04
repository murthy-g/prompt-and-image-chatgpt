import os
import openai
import re

openai.api_key = os.getenv("OPEN_API_KEY")

prompt = input("Enter your prompt: ")


def create_prompt(prompt):
    prompt = f"Create a detailed prompt query based on the {prompt}.\nAdditionally, assign a title starting with 'Title: ' to this context."
    return prompt

def extract_title(recipe):
    print(recipe);
    return re.findall("^.*Title: .*$", recipe, re.MULTILINE)[0].strip().split("Recipe Title: ")[1]

recipe_prompt = create_prompt(prompt)

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=recipe_prompt,
    max_tokens=512,
    temperature=0.7
)

result_text = response['choices'][0]['text']
title = result_text.split('Title: ')[1]

print(title)
response = openai.Image.create(
    prompt=title,
    n=1,
    size='1024x1024'
)

image_url = response['data'][0]['url']

import requests
import shutil
def save_image(image_url, file_name):
    image_res = requests.get(image_url, stream=True)
    if(image_res.status_code == 200):
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(image_res.raw, f)
    else:
        print("Couldn't save image")

    return image_res.status_code

save_image(image_url, 'test.png')