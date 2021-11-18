from twilio.rest import Client

account_sid = 'ACd9234495426c5e1444ad178062e0d95a'
auth_token = '1cbf1cf3fde158134619743de4472280'
twilio_number = '+19036182852'

def text(number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=message, from_=twilio_number, to=number)