import state
from internal_functions.functions import send
from modules.downtime import downtime
from modules.house_rules import house_rules
from modules.XP_rewards import xp_rewards
from modules.emailer.schedule_reminder_email import send_schedule_reminder_email


async def admin_router():
    if "$email" in state.message.content:
        try:
            await send("Processing emails. . .")
            send_schedule_reminder_email()
            await send("Emails sent!")
        except IndexError:
            print("Emails not sent. Index error in message.")
            await send('Emails not sent.\nEnsure your message is formatted "$email [month] [date] [month] [date]", indicating the start date and end date.\nThe spaces between the months and dates is required.')
        except TypeError as e:
            print("Exception:")
            print(e)
            await send('Emails not sent.\nEnsure months are written as words and dates as numbers.\nEg. "Nov 1 Nov 15"')
        except Exception as e:
            print("Exception:")
            print(e)
            await send('Email error. Please contact Joel. (Exception printed to console.)')
    await user_router()


async def user_router():
    if "$downtime" in state.message.content:
        await downtime()
    elif "$houserules" in state.message.content or "$rules" in state.message.content:
        await house_rules()
    elif "$xp" in state.message.content:
        await xp_rewards()

