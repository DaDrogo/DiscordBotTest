import discord
import random
import json
from discord.ext import commands

#import TOKEN from json file
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

    # Send Welcome-message, still hardcoded TODO
    async def on_member_join(self, member):
        welcome_channel = client.guilds[0].system_channel
        await welcome_channel.send('Willkommen auf dem Server '+ member.mention + ' !')



client = MyClient()
client.run(TOKEN)
