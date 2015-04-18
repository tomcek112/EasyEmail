from twilio.rest import TwilioRestClient
from flask import Flask, request , make_response

from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
from os import path

import twilio.twiml
import dataset

app = Flask(__name__)

db = dataset.connect('sqlite:///client.db')
table = db['list']

@app.route('/', methods=['GET', 'POST'])
def dataextract():
    if request.method =='POST':
        from_add = request.form['from']
        sub = request.form['subject']
        text = request.form['text']
        print(text)
        updatedb(from_add,text)
        #twil(sub,from_add,text)
        #datparser(sub,from_add,text)
        return make_response('',200)
    else:
        return "Bla"

'''def dataparser(sub,from_add,text):
    twil(sub,from_add,parsed_text)
'''

def twil(sub,from_add,text):
    account_sid = "ACd88394ca183bcaf1f02a2e8bcf5ebf55"
    auth_token = "5582a52e32afa122e7492d8a506b926d"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to="+447831002358",from_="+447903530001",body="from:"+from_add+" subject:"+sub+" body:"+ text)

def updatedb(from_add,mes):
    usr=table.find_one(from_addr=from_add)
    if usr:
        usr['messages']=usr['messages'] + mes
        table.update(dict(from_addr=from_add, messages = usr['messages']),['from_addr'])
    else:
        table.insert(dict(from_addr=from_add, messages = mes))

def wordcloud(user):
    text = user['messages']
    tags = make_tags(get_tag_counts(text), maxsize=120)
    create_tag_image(tags, './static/cloud_large.png', size=(600, 600), fontname='Cuprum')


@app.route("/respond", methods=['GET', 'POST'])
def paid_respond():
    message = request.values.get('Body')
    message_elements = message.split(' ')
    resp = twilio.twiml.Response()
    if message_elements[0].lower() == 'get':
        message_elements.pop(0)
        addr = (' ').join(message_elements)
        addr = addr[:-1]
        usr = table.find_one(from_addr=addr)
        if usr:
             wordcloud(usr)
             with resp.message("Loaded WebCloud") as m:
                 m.media("./static/cloud_large.png")
        else:
            resp.message("Contact Not Found")
    else:
        resp.message("Invalid Syntax")
    return str(resp)


if __name__ == '__main__':
    app.run(port=8000,debug=True)
