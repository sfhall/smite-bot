#smite_bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#on entering a chat
@client.event 
async def on_ready():
    print(f'{client.user} has connented to Discord!')

#handler for new memebers
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'VVGH: Hi {member.name}, welcome to the cluster fuck!'
    )

#handler for smite commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    

    if message.content == 'VVGH':
        response = 'Hi!'
    elif message.content == 'VGG':
        response =  'Gank!'
    elif message.content == 'VQN':
        response =  'Need wards!'
    elif message.content == 'VVA':
        response =  'Ok!'
    elif message.content == 'VVB':
        response = 'Be right back!'
    elif message.content == ' VVGB':
        response = 'Bye!'
    elif message.content == ' VVGO':
        response =  'Oops!'
    elif message.content == ' VVGQ':
        response =  'Quiet!'
    
    await message.channel.send(f'{message.author} says: {response}')

client.run(TOKEN)