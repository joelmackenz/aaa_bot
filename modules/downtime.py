from internal_functions.functions import send, send_private_msg
import discord
import state
client = discord.Client()


async def downtime():
    # Checks if the message is not public
    if not isinstance(state.message.channel, discord.channel.DMChannel):
        await send("Sending you a private message about downtime!")
    await send_private_msg(
        "**Downtime**\n"
        "*Last updated: 17/10/2021*\n\n"
        "Downtime is whatever happens to the character between adventures.\n"
        "Players can do all of the following things in between any game, in any order:\n\n"
        "1. **Heal** - <https://aaapathfinder.wordpress.com/downtime/#heal>\n"
        "Player normally heals up to full health and lose any negative conditions\n"
        "2. **Buy/sell items** - <https://aaapathfinder.wordpress.com/downtime/#buy-sell>\n"
        "Players can purchase as many items as they like according to the price listed in the Core"
        "Rulebook. They can sell items for half their price\n"
        "3. **Change coinage** - <https://aaapathfinder.wordpress.com/downtime/#change-coinage>\n"
        "Change coins into coins of other types (copper to silver, silver to gold, etc.). This costs nothing and can be done in any amount.\n"
        "4. **Spend XP** - <https://aaapathfinder.wordpress.com/downtime/#spend-xp>\n"
        "Spend as much or as little XP as the player likes as outlined in the XP Rewards doc. If the"
        "player increased their level, they apply changes to their character.\n"
        "5. **Select a Downtime Activity** - <https://aaapathfinder.wordpress.com/downtime/#select-activity>\n"
        "• Auction an item with Drecker & Dee\n"
        "• Ask Zoltan for your future with Drecker & Dee\n"
        "• Craft an item\n"
        "• Earn income\n"
        "• Recall knowledge\n"
        "• Gather info\n"
        "• Gamble\n"
        "• Retrain\n"
        "• Patrol\n"
        "• Relax\n\n"
        "For more info, go to <https://aaapathfinder.wordpress.com/downtime>"
    )
