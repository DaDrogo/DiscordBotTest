import discord
from discord.ext import commands

TOKEN='NjE3NzU3MzM2NjcyNTM0NTk4.XWvzMQ.Hx_wd4tSadFPzMzHT3PRpxqQp1A'

client = commands.Bot(command_prefix='test')

@client.event
async def on_ready():
    print('bot is rdy.')

client.run(TOKEN)
    