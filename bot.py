from ast import If
import discord
import random
from decouple import config

TOKEN =  config('DISCORD_API_KEY')

intents = discord.Intents.default()
intents.message_content = True

responses = ['yes','no','try asking again'] #1/3 Equal chance of yes, no and re-roll
negativeResponses= ['no','no','maybe someday',"I don't think so"] # 50% chance default no, 25% each alternate

client = discord.Client(intents = intents)

def conch_decide(message_string):
    print(message_string)
    try:
        choice = random.choice(responses)
        if choice == 'no':
            choice = random.choice(negativeResponses)
        return choice
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