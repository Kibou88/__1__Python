import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv() #Charger le fichier
# Si fichier autre que '.env' mettre load_dotenv(dotenv_path="file")

# Initialiser le bot avec un préfixe de commande
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Événement qui se déclenche lorsque le bot est prêt
# Le décorateur @bot.event permet d'indiquer que la fonction on_ready est une fonction qui doit recevoir
# les informations envoyées lorsque l'événement est appelé par Discord
@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')

    
# Commande simple qui répond avec "Pong!"
@bot.command(name='del')
# ctx: contexte (par convention) permet de récupérer le salon
async def delete(ctx, number_of_messages: int):
    messages = []
    async for message in ctx.channel.history(limit=number_of_messages + 1):
        messages.append(message)

    for each_message in messages:
        await each_message.delete()

@bot.command(name='history')
async def history(ctx):
    await ctx.channel.send(ctx.channel.history())

# Exécuter le bot avec le token récupéré dans le fichier .env
bot.run(os.getenv('DISCORD_API_KEY'))
