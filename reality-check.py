import os
import random
import time
from twilio.rest import Client

MESSAGE_PROB = 0.5
MSG_LIMIT = 3   # guarunteed to get one message at least every 3 hours
FREQ = 3600 # in seconds

START_HOUR = 9
END_HOUR = 23

f = open('shhh', 'r')
secret = f.read().splitlines()
f.close()

account_sid = secret[0]
auth_token = secret[1]
twilio_number = secret[2]

reality_check_message = [
    'PUT YOUR HANDS IN THE AIR\nTHIS IS A REALITY CHECK', 
    'rEaLiTy ChEcK', 
    'reality check', 
    'psst...\n\n\n\n\n\n\n\n\n\n\n...reality check', 
    'can i get uhhh... reality check',
    'never gonna give you up, never gonna let you forget your reality check',
    'reality check yourself before you reality wreck yourself',
    'look at your hands (reality check)',
    'REALITY CHECK MOTHERFUCKER',
    'something something reality check',
    'reply STOP to stop getting reality check reminders\n\nbtw this is not a joke i think the STOP command works',
    'what time is it? REALITY CHECK TIME!',
    'when i say REALITY you say CHECK',
    'this is the time where you check your reality',
    'nobody expects the spanish reality check',
    '\'tis but a reality check',
    'MERRY CHRISTMAS\nSanta brought you a reminder for a reality check',
    'QUICKLY! STOP, DROP, AND reality check',
    'reality check babyyyyy',
    "it's a bird, it's a plane——jk, it's a reality check",
    "this is the reality man coming to bestow upon you a reality check",
    'hey kid, you want a reality check?',
    'REALITYYYYYYYYYYYYYYY check',
    'i can show you the reality check... shining shimmERING SPLENDID',
    'get a BUCKET and a REALITY CHECK',
    "so this reality check is obviously very heartfelt to me because uhh... i'm Addison Rae",
    "g i v e  u s  t h e  r e a l i t y  c h e c k",
    "mannnnn reality check",
    "you call me gay?\nno\nwell then i reality check",
    "mom come pick me up i need a reality check",
    "OH BABY A REALITY CHECK AWWW YEAAA",
    "hello everybody this is JettStreams and today we're playing REALITY CHECK",
    "please sign here for your reality check",
    "yes, hello, i would like a #10 large meal with a coke, 2 mcchickens, a large fry and a reality check thanks",
    "Keep Calm and Reality Check.",
    "you seen any reality checks around here?",
    "A long time ago in a reality check far, far away...",
    "happy fEET.. REALITY CHECK"
]

f = open('phone-numbers', 'r')
numbers = f.read().splitlines()
f.close()

prev_messages = [[] for _ in numbers]
no_msg_count = [0 for _ in numbers]

def choose_message(prev, message_list):
    message = random.choice(reality_check_message)

    while (message in prev):
        message = random.choice(reality_check_message)
    
    prev.append(message)

    if (len(prev) > 5):
        del prev[0]
    
    return message

def send_reality_check():
    client = Client(account_sid, auth_token)

    curr_hour = time.localtime().tm_hour
    curr_min = time.localtime().tm_min
    for i, number in enumerate(numbers):
        prob = random.random()

        if curr_hour >= START_HOUR and curr_hour <= END_HOUR:
            if (prob > MESSAGE_PROB) or (no_msg_count[i] >= 3):
                no_msg_count[i] = 0
                print('Message sent to %s at %02d:%02d' % (number, curr_hour, curr_min))
                message = choose_message(prev_messages[i], reality_check_message)
                client.messages.create(body=message, from_=twilio_number, to=number)
            else:
                no_msg_count[i] += 1

while True:
    send_reality_check()
    time.sleep(FREQ)