import state
from modules.downtime import downtime
from modules.emailer.email_schedule_reminder import send_email


async def admin_router():
    if "$mail" in state.message.content:
        await send_email()


async def user_router():
    if "$downtime" in state.message.content:
        await downtime()
