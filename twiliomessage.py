from twilio.rest import TwilioRestClient

number = raw_input("Enter a Phone Number:")
message = raw_input("Enter Message:")
account_sid = "ACd88394ca183bcaf1f02a2e8bcf5ebf55"
auth_token = "5582a52e32afa122e7492d8a506b926d"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(to=number,from_=" 447903530001",body=message)
