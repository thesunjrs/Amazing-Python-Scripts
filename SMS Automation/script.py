from twilio.rest import Client

api = input("Enter your ACCOUNT SID: ")
auth = input("Enter your AUTH TOKEN: ")
from_number = input("Enter number from which you want to send the SMS: ")
message = input("Enter the massage: ")
to_number = input(
    "Enter comma separated numbers to which you want to send the SMS: ")
lists = to_number.split(",")
groupnum = list(lists)
account_sid = api
auth_token = auth
client = Client(account_sid, auth_token)

for item in groupnum:
    client.messages.create(from_=from_number, body=message, to=item)
