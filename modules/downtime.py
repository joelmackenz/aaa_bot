from functions.functions import send, send_private_msg
import discord
import state
client = discord.Client()


async def downtime():
    # Checks if the message is not public
    if not isinstance(state.message.channel, discord.channel.DMChannel):
        await send("Sending you a private message!")
    await send_private_msg(
        "**Downtime Info**\n"
        "*Last updated: 17/10/2021*\n"
        "Downtime is whatever happens to the character between adventures.\n"
        "Players can do all of the following things in between any game, in any order:\n"
        "1. Heal\n"
        "2. Buy and sell items.\n"
        "3. Change coinage. This can be done freely, with no commissions charged.\n"
        "4. Spend XP.\n"
        "5. Select a downtime activity.\n"
        "**Heal** - <https://aaapathfinder.wordpress.com/downtime/#heal>\n"
        "Player normally heals up to full health and lose any negative conditions\n"
        "**Buy/sell items** - <https://aaapathfinder.wordpress.com/downtime/#buy-sell>\n"
        "Players can purchase as many items as they like according to the price listed in the Core"
        "Rulebook. They can sell items for half their price\n"
        "**Change coinage** - <https://aaapathfinder.wordpress.com/downtime/#change-coinage>\n"
        "Change coins into coins of other types (copper to silver, silver to gold, etc.). This costs nothing"
        "and can be done in any amount.\n"
        "**Spend XP** - <https://aaapathfinder.wordpress.com/downtime/#spend-xp>\n"
        "Spend as much or as little XP as the player likes as outlined in the XP Rewards doc. If the"
        "player increased their level, they apply changes to their character.\n"
        "**Select a Downtime Activity** - <https://aaapathfinder.wordpress.com/downtime/#select-activity>\n"
        "These include: play a Drecker & Dee game, craft an item, earn income, recall knowledge, gather info, run a business, gamble, retrain, patrol, and relax.\n"
        "For more info on any item, press on any link to go to the Official AAA Website - <https://aaapathfinder.wordpress.com>"
    )
