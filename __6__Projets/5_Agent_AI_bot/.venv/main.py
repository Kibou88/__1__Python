# FHcEfijpEWc6OL4zhoP732dTlEyPSvg1

import os
from mistralai import Mistral
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

async def message_to_Mistral(api_key_mistral, model, message):
    client = Mistral(api_key=api_key_mistral)

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

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')


@bot.event
async def on_message(message):
    print(message.content)
    return message.content.lower()

async def receive_message(raw_message, message_mistral):
    if message_mistral:
        await raw_message.channel.send(message_mistral)

if __name__ == '__main__':
    api_key_mistral = os.environ["MISTRAL_API_KEY"]
    model = "mistral-large-latest"

    on_ready()
    bot.run(os.environ["DISCORD_API_KEY"])

    message_discord = on_message(message)
    print(message_discord)
    message_mistral = message_to_Mistral(api_key_mistral, model, message_discord)
    print(message_mistral)
    receive_message(raw_message, message_mistral)
