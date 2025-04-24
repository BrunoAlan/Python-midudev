import os
from os import system
import requests

if system("clear") != 0:
    system("cls")

from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPEN_AI_API_KEY")


def call_openai_gpt(api_key, prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        print(result["choices"][0]["message"]["content"])
    else:
        print(f"Error: {response.status_code} - {response.text}")


call_openai_gpt(api_key, "Escribime un poema sobre la programación")
