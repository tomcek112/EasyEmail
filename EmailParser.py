from twilio.rest import TwilioRestClient
from flask import Flask, request , make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dataextract():
    if request.method =='POST':
        from_add = request.form['from']
        sub = request.form['subject']
        text = request.form['text']
        datparser(sub,from_add,text)
        return make_response('',200)
    else:
        return "Bla"

def dataparser(sub,from_add,text):
    twil(sub,from_add,parsed_text)


def twil(sub,from_add,text):
    account_sid = "ACd88394ca183bcaf1f02a2e8bcf5ebf55"
    auth_token = "5582a52e32afa122e7492d8a506b926d"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to="+4407947771680",from_="+447903530001",body="from:"+from_add+" subject:"+sub+" body:"+ text)

if __name__ == '__main__':
    app.run(port=8000,debug=True)