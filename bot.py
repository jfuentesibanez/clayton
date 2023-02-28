# bot.py
import os
import discord
from dotenv import load_dotenv
import openai

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

openai.api_key = OPENAI_KEY

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# trying to modify the code to respond only to the bot mention
@client.event
async def on_message(message):

  # Bot personality
  personality = "A continuación se muestra una conversación con asistente virtual. El nombre del asistente virtual es Clayton, es inteligente, agradable y es experto en innovación corporativa. Siempre contestas de manera amable y cuando se le dice hola siempre responde ¿cómo te puedo ayudar?."
  
  
  # Only respond to messages from other users, not from the bot itself
  if message.author == client.user:
    return
  
  # Check if the bot is mentioned in the message
  if client.user in message.mentions:
 
    # Use the OpenAI API to generate a response to the message
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"{personality}\n{message.content}",
    max_tokens=2048,
    temperature=0.8,
    )

  # Send the response as a message
  await message.channel.send(response.choices[0].text)

# start the bot
client.run(TOKEN)



