from dotenv import load_dotenv
import google.generativeai as genai
import discord
import os

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

def call_gemini(question):
    prompt = f"Respondendo com o AI_Teste_1: {question}"
    response = model.generate_content(prompt)
    return response.text

#intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print ('Estamos logados como {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$ola'):
        await message.channel.send('Olá, tudo bom?')

    if message.content.startswith('$hello'):
        await message.channel.send('Olá, tudo bom? Meus comandos são em português, então use $ola e $pergunta ;)')

    if message.content.startswith('$question'):
        await message.channel.send('Olá, tudo bom? Meus comandos são em português, então use $ola e $pergunta ;)')

    if message.content.startswith('$pergunta'):
       print(f"Mensagem recebida: {message.content}")
       message_content = message.content.replace("$pergunta", "").strip()
       response = call_gemini(message_content)
       print(f"Assistente: {response}")
       print("---")
       await message.channel.send(response)

client.run(os.getenv('TOKEN'))

         



