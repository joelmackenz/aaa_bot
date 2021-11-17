from internal_functions.functions import send, send_private_msg
import discord
import state
client = discord.Client()


async def xp_rewards():
    # Checks if the message is not public
    if not isinstance(state.message.channel, discord.channel.DMChannel):
        await send("Sending you a private message about XP rewards!")
    await send_private_msg(
        "**XP Rewards**\n"
        "*Last updated: 14/08/2021*\n\n"

        "AAA uses a simplified method of levelling up that primarily rewards players for **playing** and **engaging with** the game.\n\n"

        "Earning XP: - <https://aaapathfinder.wordpress.com/xp-rewards#earning-xp>\n"
        "1. Playing a session: 10 XP\n"
        "2. Writing/Creating an after-action report: 5 XP\n"
        "3. Contributing to the session in the real world: 3 XP\n\n"

        "Exchanging XP: - <https://aaapathfinder.wordpress.com/xp-rewards#exchanging-xp>\n"
        "1. **Level up**: costs 10x the player’s current level to level up to the next.\n"
        "2. **Windfall**: exchange XP for GP, at 1 XP for 10 GP.\n"
        "3. **Raise dead**: raise the body of a recovered ally for 5 XP.\n"
        "4. **Start a business**: establish a business in town for 10 XP (see link for more details).\n"
        "5. **Improve the town**: spend XP in multiples of 10 to improve the town (see link for more details).\n\n"

        "For more info, go to <https://aaapathfinder.wordpress.com/xp-rewards>"
    )
