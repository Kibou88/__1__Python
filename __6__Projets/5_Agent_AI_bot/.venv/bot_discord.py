import discord
from discord.ext import commands

# Initialiser le bot avec un préfixe de commande
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Événement qui se déclenche lorsque le bot est prêt
# Le décorateur @bot.event permet d'indiquer que la fonction on_ready est une fonction qui doit recevoir
# les informations envoyées lorsque l'événement est appelé par Discord
@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')

@bot.event
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("Pong!")


# Exécuter le bot avec le token
bot.run(TOKEN)
