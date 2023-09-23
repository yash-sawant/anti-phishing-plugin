import requests
from secrets import API_TOKEN


API_URL = "https://api-inference.huggingface.co/models/foghlaimeoir/phishing-DistilBERT"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": "I like you. I love you",
})