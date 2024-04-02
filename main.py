from openai import OpenAI
import requests
from dotenv import load_dotenv
import os

load_dotenv()
OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")
AI_DEVS_KEY = os.getenv("AIDEVS_API_KEY")

EMBEDDINGS = "https://api.openai.com/v1/embeddings"
TOKEN = "https://tasks.aidevs.pl/token/embedding"
ANSWER = "https://tasks.aidevs.pl/answer"
TASK = "https://tasks.aidevs.pl/task"
TOKEN_PARAMS = {
    "apikey": AI_DEVS_KEY
}

token_response = requests.post(url=TOKEN, json=TOKEN_PARAMS)
token_response.raise_for_status()
token_data = token_response.json()
token = token_data["token"]

get_task_response = requests.get(url=f"{TASK}/{token}")
token_response.raise_for_status()
task_data = get_task_response.json()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPEN_AI_KEY}"
}

body = {
    "input": "Hawaiian pizza",
    "model": "text-embedding-ada-002"
}

response = requests.post(url=EMBEDDINGS, headers=headers, json=body)
response.raise_for_status()
response_data = response.json()
print(response_data["data"][0]["embedding"])

answer = {
    "answer": response_data["data"][0]["embedding"]
}

send_answer = requests.post(url=f"{ANSWER}/{token}", json=answer)
send_answer.raise_for_status()