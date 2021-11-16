
import json
import os
import state
from internal_functions.functions import send
from dotenv import load_dotenv

load_dotenv()

from quickstart import main
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

service = main()

def send_schedule_reminder_email():
    # TODO For entries in email list, send one email, include name as variable
    email_list = json.loads(os.getenv("EMAIL_LIST"))    

    split_message = state.message.content.split()

    try:
        int(split_message[2]) and int(split_message[4])
    except:
        raise Exception("Month and date string not written in correct format: str int str int.")

    try:
        int(split_message[1]) and int(split_message[3])
    except:
        for user_name in email_list:
            email_addr = email_list[user_name]
            start_date = split_message[1].capitalize() + " " + split_message[2]
            end_date = split_message[3].capitalize() + " " + split_message[4]

            email_body = "<p>Hey, " + user_name + "!<br><br><b>A new schedule has been posted</b> for AAA Pathfinder, for the week of <b>" + start_date + "</b> to <b>"+ end_date +"</b>!<br><br>Head over to Discord to check it out!<br><br>Sincerely,<br>Apelus Adevnturer's Association Bot<br><br><br><br><i>For safety's sake, this bot does not include links in emails. If you do see a link in an email from AAA Bot, tell an adult immediately. Or message Joel.</i></p>"

            Message = MIMEMultipart()
            Message['to'] = email_addr
            Message['subject'] = "A new AAA Schedule poll was posted!"
            Message.attach(MIMEText(email_body, 'html'))
            raw_string = base64.urlsafe_b64encode(Message.as_bytes()).decode()
            service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
            print("Email message successfully sent!")
   