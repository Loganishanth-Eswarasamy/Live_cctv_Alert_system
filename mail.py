import smtplib
from email.message import EmailMessage

# content
sender = "sendermail"
reciever = "reciever mail"
password = "password"
msg_body = '''Camera Alert
         venue: channerl Camera
lounge
         time: 6 pm
         date: 18 october 2020
         Image
        '''

# action
msg = EmailMessage()
msg['subject'] = 'Security Alert'
msg['from'] = sender
msg['to'] = reciever
msg.set_content(msg_body)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender, password)

    smtp.send_message(msg)