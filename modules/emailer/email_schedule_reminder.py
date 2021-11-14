
import json
import os
from dotenv import load_dotenv

load_dotenv()

from quickstart import main
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

service = main()

def send_email(service, subject, message):
    # TODO For entries in email list, send one email, include name as variable
    # include var for dates of next sesh
    
    email_list = json.loads(os.getenv("EMAIL_LIST"))    

    emailMsg = message
    Message = MIMEMultipart()
    Message['to'] = email_list[0]
    Message['subject'] = subject
    Message.attach(MIMEText(emailMsg, 'html'))
    raw_string = base64.urlsafe_b64encode(Message.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    return message

send_email(service, "A new AAA Schedule poll was posted!", 
"<h1>this is a test message</h1>\nWith <i>some</i> formatting\n<h2>Have a great evening!</h2>"
)
