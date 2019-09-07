import discord
import random
from discord.ext import commands

TOKEN=''
client = commands.Bot(command_prefix='test')
rnd = random.randint(1,1000)


@client.event
async def on_ready():
    print('bot is rdy.')
    
@client.event
async def on_message(message):
    if message.content.startswith('!test'):        
        await message.channel.send('hello world!')
        await message.channel.send('hello world!')
    if message.content.startswith('!rnd'):
        await message.channel.send(rnd)
    if message.content.startswith('!magic'):
        rndAnswe = random.randint(1,2)
        if rndAnswe == 1:
            answer = 'yes'
        else:
            answer = 'no' 
        await message.channel.send(rndAnswe)
        await message.channel.send(answer)
        
    
client.run(TOKEN)
    