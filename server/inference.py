import requests
from secrets import API_TOKEN


API_URL = "https://api-inference.huggingface.co/models/foghlaimeoir/phishing-DistilBERT"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(text):
    payload = {
        "inputs": text,
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


if __name__ == "__main__":

    output = query('Are you interested in joining a pyramid scheme?')

    print(output)