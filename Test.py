import discord
import random
import json
from discord.ext import commands

#import TOKEN from json
with open('secrets.json', 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)
TOKEN=obj['secret_token']

client = commands.Bot(command_prefix='test')
rnd = random.randint(1,1000)

@client.event
async def on_ready():
    print('bot is rdy.')
    
@client.event
async def on_message(message):
    # don't respond to ourselves
    #if message.author == self.user:
       #return

    if message.content.startswith('!test'):        
        await message.channel.send('hello world!')
        await message.channel.send('hello world!')
    if message.content.startswith('!rnd'):
        rnd = random.randint(1,1000)
        await message.channel.send(rnd)
    if message.content.startswith('!magic'):
        rndAnswe = random.randint(1,2)
        if rndAnswe == 1:
            answer = 'yes'
        else:
            answer = 'no' 
        await message.channel.send(rndAnswe)
        await message.channel.send(answer)
    if message.content.startswith('!hello'):
        channel = message.channel
        await channel.send('hello')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message',check=check)
        await channel.send('Hello {.author} !'.format(msg))
        
    
client.run(TOKEN)
    