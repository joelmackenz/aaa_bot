
import json
import os
import state
from dotenv import load_dotenv

load_dotenv()

from quickstart import main
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

service = main()

def send_custom_email():
    email_list = json.loads(os.getenv("LIVE_EMAIL_LIST"))    

    custom_message = state.message.content.split(' ', 1)[1] #Removes first word of msg (which is the command to send message)

    for user_name in email_list:
        email_addr = email_list[user_name]

        email_body = "<p>Hey, " + user_name + "!<br><br><b>Your DMs have sent you a custom message for AAA Pathfinder:</b><br><br> " + custom_message + "<br><br>Head over to Discord to get in on the action!<br><br>Sincerely,<br>Apelus Adventurer's Association Bot<br><br><br><br><i>For safety's sake, this bot does not include links in emails. If you do see a link in an email from AAA Bot, tell an adult immediately. Or message Joel.</i></p>"

        Message = MIMEMultipart()
        Message['to'] = email_addr
        Message['subject'] = "New message from the AAA DMs!"
        Message.attach(MIMEText(email_body, 'html'))
        raw_string = base64.urlsafe_b64encode(Message.as_bytes()).decode()
        service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
        print("Email message successfully sent to " + email_addr + "!")
   