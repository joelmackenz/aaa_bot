from internal_functions.functions import send, send_private_msg
import discord
import random
import state
client = discord.Client()


async def fun_fact():

    fun_facts = [
        "If you and your ally **flank** an opponent, and are both able and willing to attack with melee weapons, the enemy takes on the flat-footed trait, taking a -2 circumstance penalty to AC\n*Core Rulebook pg 476*",
        "If you take cover, you attain a +1, +2, or +4 circumstance bonus to AC, reflex saves, and stealth checks to hide, sneak, or avoid detection!\nCover comes in three types: lesser (+1, typically behind a person); standard (+2); and Greater (+4)!\n*Core Rulebook pg 477*",
        "You can hold your breath for a number of rounds equal to 5 + your Constitution modifier!\n*Core Rulebook pg 478*"
    ]

    random_fact = fun_facts[random.randint(0, len(fun_facts))]

    # Checks if the message is not public
    if not isinstance(state.message.channel, discord.channel.DMChannel):
        await send("Sending you a fun Pathfinder fact!")
    await send_private_msg(
        "**Fun Fact**\n\n" + random_fact
    )
