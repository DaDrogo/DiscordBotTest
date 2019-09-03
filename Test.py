import discord
from discord.ext import commands

TOKEN='NjE3NzU3MzM2NjcyNTM0NTk4.XW3Ldw.qUmwIfFT07JflovTnzIjHAvuGZA'

client = commands.Bot(command_prefix='test')

@client.event
async def on_ready():
    print('bot is rdy.')
    
@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await message.channel.send('hello world!')
    
client.run(TOKEN)
    