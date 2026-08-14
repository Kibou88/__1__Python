import os
import discord
import aiohttp
from dotenv import load_dotenv
from discord.ext import commands
from mistralai import Mistral

load_dotenv()

class DiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.all())

    async def on_ready(self):
        print(f'Bot {self.user.display_name} connected to Discord!')

    async def on_message(self, message):
        # Évitez de traiter les messages du bot lui-même pour éviter les boucles
        if message.author == self.user:
            return

        print(f"Message reçu: {message.content}")

        # Envoyer le message à l'API de Mistral
        # await self.send_to_mistral_api(message.content)
        await self.send_to_mistral(message)

        # Assurez-vous de traiter les commandes du bot
        await self.process_commands(message)

    async def send_to_mistral_api(self, message_content):
        url = "https://api.mistral.ai/endpoint"  # Remplacez par l'URL réelle de l'API
        headers = {
            "Authorization": "Bearer FHcEfijpEWc6OL4zhoP732dTlEyPSvg1",  # Remplacez par votre clé API
            "Content-Type": "application/json"
        }
        data = {
            "content": message_content
        }

    async def send_to_mistral(self, message_content):
        client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

        chat_response = client.chat.complete(
            model="mistral-large-latest",
            messages=[
                {
                    "role": "user",
                    "content": message_content.content,
                },
            ]
        )
        print(chat_response.choices[0].message.content)
        await message_content.channel.send(chat_response.choices[0].message.content)

        async with aiohttp.ClientSession() as session:
            pass
            # async with session.post(url, headers=headers, json=data) as response:
            #     if response.status == 200:
            #         response_data = await response.json()
            #         print("Réponse de l'API:", response_data)
            #     else:
            #         print("Erreur lors de l'envoi du message à l'API:", response.status)

# Instanciation et exécution du bot
kurama_doc_bot = DiscordBot()
kurama_doc_bot.run(os.getenv('DISCORD_API_KEY'))
