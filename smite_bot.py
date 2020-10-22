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
    
    #attack commands
    if message.content.upper() == 'VA1':
        response = 'Attack left lane!'
    elif message.content.upper() == 'VA2':
        response = 'Attack middle lane!'
    elif message.content.upper() == 'VA3':
        response = 'Attack right lane!'
    elif message.content.upper() == 'VAA':
        response = 'Attack!'
    elif message.content.upper() == 'VAF':
        response = 'Attack Fire Giant!'
    elif message.content.upper() == 'VAG':
        response = 'Attack the Gold Fury!'
    elif message.content.upper() == 'VAM':
        response = 'Attack the Titan!'
    #attack the phonixes/towers

    #MIA commands
    elif message.content.upper() == 'VF1':
        response = 'Enemy missing left!'
    elif message.content.upper() == 'VF2':
        response = 'Enemy missing middle!'
    elif message.content.upper() == 'VF3':
        response = 'Enemy missing right!'
    elif message.content.upper() == 'VFF':
        response = 'Enemy missing!'
    
    #help
    elif message.content.upper() == 'VHH':
        response = 'Help!'
    elif message.content.upper() == 'VHS':
        response = 'Need healing!'

    #im...
    elif message.content.upper() == 'VSO':
        response = 'Im on it!'
    elif message.content.upper() == 'VSS':
        response = 'Im building stacks!'

    #other
    elif message.content.upper() == 'VVGH':
        response = 'Hi!'
    elif message.content.upper() == 'VVGF':
        response = 'Have Fun!'
    elif message.content.upper() == 'VVGG':
        response = 'Good Game!'
    elif message.content.upper() == 'VVGL':
        response = 'Good luck!'
    elif message.content.upper() == 'VVGN':
        response = 'Nice Job!'
    elif message.content.upper() == 'VGG':
        response =  'Gank!'
    elif message.content.upper() == 'VQN':
        response =  'Need wards!'
    elif message.content.upper() == 'VVA':
        response =  'Ok!'
    elif message.content.upper() == 'VVB':
        response = 'Be right back!'
    elif message.content.upper() == 'VVGB':
        response = 'Bye!'
    elif message.content.upper() == 'VVGO':
        response =  'Oops!'
    elif message.content.upper() == 'VVGQ':
        response =  'Quiet!'
    
    #the holy ones
    elif message.content.upper() == 'VVP':
        response = 'Please'
    elif message.content.upper() == 'VVN':
        response = 'No!'
    elif message.content.upper() == 'VER':
        response = 'You rock!'
    elif message.content.upper() == 'VVX':
        response = 'Cancel That!'
    elif message.content.upper() == 'VVVW':
        response = 'Place a ward for teleport!'
    elif message.content.upper() == 'VVGT':
        response = 'Thats too bad!'

    await message.channel.send(f'{message.author} says: {response}')

client.run(TOKEN)