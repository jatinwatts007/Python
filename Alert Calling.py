from twilio.rest import Client

account_sid = 'ACa8282127b4fa9759c410e6b772add3f8'
auth_token = '7500d040207224f52a29990ff29d1080'
client = Client(account_sid,auth_token)
call = client.calls.create(
    twiml='<Response><Say>Hello snapchat family.................................</Say></Response>',
    to='+919610830608', from_=+17404869638
)
print(call.sid)
