import discord
import random
from decouple import config

TOKEN =  config('DISCORD_API_KEY')

intents = discord.Intents.default()
intents.message_content = True

responses = ['yes','no','maybe someday','try asking again']

client = discord.Client(intents = intents)

def conch_decide(message_string):
    print(message_string)
    try:
        return random.choice(responses)
    except:
        return "Try asking again"

@client.event
async def on_ready():
    print("Ready! {}".format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith('oh magic conch'):
        await message.channel.send(conch_decide(message.content))
    
client.run(TOKEN)