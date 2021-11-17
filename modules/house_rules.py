from internal_functions.functions import send, send_private_msg
import discord
import state
client = discord.Client()


async def house_rules():
    # Checks if the message is not public
    if not isinstance(state.message.channel, discord.channel.DMChannel):
        await send("Sending you a private message about the house rules!")
    await send_private_msg(
        "**House Rules**\n"
        "*Last updated: 14/10/2021*\n\n"
        
        "House rules are fun rules that we came up with!\n"
        "The following rules apply during any game:\n\n"
        
        "1. **Simultaneous Initiative** - <https://aaapathfinder.wordpress.com/house-rules#simultaneous-initiative>\n"
        "Two players can attack at the same time.\n"
        "2. **Death** - <https://aaapathfinder.wordpress.com/house-rules#death>\n"
        "Death triggers a final stand, and one must decide what to do with their items.\n"
        "3. **Final Stand** - <https://aaapathfinder.wordpress.com/house-rules#final-stand>\n"
        "One final action, at the GM's discretion.\n"
        "4. **Hot or Not?** - <https://aaapathfinder.wordpress.com/house-rules#hot-or-not>\n"
        "Roll a d10 for any PC or NPC to determine their hotness level.\n"
        "5. **Flashback** - <https://aaapathfinder.wordpress.com/house-rules#flashback>\n"
        "Spent a hero point to ret-con in a way that benefits your situation.\n"
        "6. **The Devil's Bargain** - <https://aaapathfinder.wordpress.com/house-rules#the-devils-bargain>\n"
        "Take a d20 roll at the cost of a dire consequence.\n"
        "7. **Player vs Player Combat** - <https://aaapathfinder.wordpress.com/house-rules#player-vs-player-combat>\n"
        "None allowed (at least to start).\n"
        "8. **Evil Characters** - <https://aaapathfinder.wordpress.com/house-rules#evil-characters>\n"
        "Evil characters force the player to lose control of them.\n"
        "9. **Spell Ingredients** - <https://aaapathfinder.wordpress.com/house-rules#spell-ingredients>\n"
        "Unless elaborate, dunworryaboutit.\n"
        "10. **Surrendered opponents and bounties** - <https://aaapathfinder.wordpress.com/house-rules#surrendered>\n"
        "Claim bounties at nearby towns for prisoners.\n\n"

        "For more info, go to <https://aaapathfinder.wordpress.com/house-rules>"
    )
