#!/usr/bin/python3.9.7
import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

# Bot sign in
@client.event
async def on_ready():
    print('{0.user}'.format(client) + ' logged in!')

# Message Responses
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send("hello world")

client.run(os.getenv('TOKEN'))