import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import asyncio

load_dotenv()

# bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
# bot.run(os.getenv('DISCORD_API_KEY'))

class DiscordBot(commands.Bot):

    def __init__(self):
        # Initialisation du bot
        super().__init__(command_prefix='!', intents=discord.Intents.all())
    async def on_ready(self):
        print(f'Bot {self.user.display_name} connected to Discord!')

    async def on_message(self, message):
        # print(self.message.content.lower())
        if message.content.lower() == "ping":
            await message.channel.send("pong")

kurama_doc_bot = DiscordBot()

kurama_doc_bot.run(os.getenv('DISCORD_API_KEY'))
