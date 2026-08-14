import os
from mistralai import Mistral
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": "python code hello world",
        },
    ]
)
print(chat_response.choices[0].message.content)