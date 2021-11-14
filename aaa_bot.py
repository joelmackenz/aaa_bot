#!/usr/bin/python3.9.7
import discord
import os
import state
import json
from state import init_state
from dotenv import load_dotenv
from router.router import admin_router, user_router

# Gmail auth
from quickstart import main
service = main()


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

    if message.author.id in json.loads(os.getenv("ADMIN_ID_LIST")):
        await admin_router()
    
    else:
        await user_router()

    state.message = {}

client.run(os.getenv('TOKEN'))