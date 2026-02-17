from dotenv import load_dotenv
import discord
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logado em {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ola'):
        await message.channel.send('Olá, tudo bom?')

client.run(os.getenv('TOKEN'))
