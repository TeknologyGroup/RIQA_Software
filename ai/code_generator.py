import requests
import os
from dotenv import load_dotenv

load_dotenv()

def generate_code(prompt):
    headers = {"Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}"}
    payload = {"inputs": prompt}
    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1",
        headers=headers,
        json=payload
    )
    return response.json()[0]['generated_text']