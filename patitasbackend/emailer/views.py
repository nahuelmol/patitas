from django.shortcuts import render

import pickle
import os.path
import mimetypes
import base64

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


SCOPES = ['https://mail.google.com/']

def get_service():
    creds = None

    PICKLE_PATH = os.getcwd() + '\\emailer\\token.pickle'
    CREDS_PATH 	= os.getcwd() + '\\emailer\\credentials.json'

    if os.path.exists(PICKLE_PATH):
        with open(PICKLE_PATH, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(PICKLE_PATH, 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    return service

def send_message(service,user_id,message):
    try:
        message = service.users().messages().send(userId=user_id,body=message).execute()
        print('Message id')
        return message
    except Exception as e:
        print('an error occured in views line 45:{}',e)
        return None

def create_message_with_attachment(sender,to,subject,body):
    message = MIMEMultipart()

    msg_content_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>My Title</title>
    <link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/superhero/bootstrap.min.css">
    <style type="text/css">
      span.bold {font-weight: bold;}
      table.noborder {border: 0px; padding: 8px;}
      th {text-align: left;}
    </style>
     </head>
    <body>
    <div class="container">
        <p>
        Click on the button below to verify your patitas account
        </p>
        <a href="http://localhost:8000/user/verify_user_by_email" type="button" class="btn btn-success">Verify</button>
    </div>
    
    </body>
    </html>
    """

    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    html_part   = MIMEText(msg_content_html, 'html')

    message.attach(html_part)
    
    raw_msg = base64.urlsafe_b64encode(message.as_string().encode('utf-8'))

    return {'raw':raw_msg.decode('utf-8')}