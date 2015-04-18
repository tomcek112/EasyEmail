import unirest
from twilio.rest import TwilioRestClient
from flask import Flask, request , make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dataextract():
    if request.method =='POST':
        from_add = request.form['from']
        sub = request.form['subject']
        text = request.form['text']
        resp(text)
   #     datparser(sub,from_add,text)
        return make_response('',200)
    else:
        return "Bla"

def resp(body):
    response = unirest.post("https://textanalysis.p.mashape.com/textblob-noun-phrase-extraction",
      headers={
        "X-Mashape-Key": "tb0NKUuhy7mshsTSq5TsvEq9Tf6gp1m4NAKjsnWO4ewgznNE9j",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    },
    params={
      "text": body 
      }
    )            

if __name__ == '__main__':
    app.run(port=8000,debug=True)