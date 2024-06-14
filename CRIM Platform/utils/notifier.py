import smtplib
from twilio.rest import Client

def send_email(recipient, subject, body):
    sender = 'your_email@example.com'
    password = 'your_password'
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(sender, recipient, message)

def send_sms(to, body):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=body, from_='+1234567890', to=to)
    return message.sid
