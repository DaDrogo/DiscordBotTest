import discord
import random
import json
from discord.ext import commands

#import TOKEN from json
with open('secrets.json', 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)
TOKEN=obj['secret_token']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run(TOKEN)