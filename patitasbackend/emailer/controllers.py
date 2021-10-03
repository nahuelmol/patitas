from django.test import TestCase
from emailer.views import get_service, send_message, create_message_with_attachment

import os

def sendmessage(email_to):
	service = get_service()
	user_id = 'me'
	sender = 'kindermolina98@gmail.com'
	to = email_to 
	subject = 'THIS IS FROM BOT'
	body = 'I do not have ideas to write about'
    
	msg = create_message_with_attachment(sender,to,subject,body)
	send_message(service,user_id,msg)

if __name__ == '__main__':
	#sendmessage()
	print(os.getcwd() + '\\example')
