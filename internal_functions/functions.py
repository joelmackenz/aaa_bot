import state

async def send(m):
    await state.message.channel.send(m)

async def send_private_msg(m):
    await state.message.author.send(m)