#!/usr/bin/python3.9.7
import discord
import os
import state
from state import init_state
from dotenv import load_dotenv
from modules.downtime import downtime

load_dotenv()
client = discord.Client()

# Bot sign in
@client.event
async def on_ready():
    print('{0.user}'.format(client) + ' logged in!')
    init_state()

# Message Responses
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    state.message = message

    if "$downtime" in message.content:
        await downtime()

    state.message = {}

client.run(os.getenv('TOKEN'))