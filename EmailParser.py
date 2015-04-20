from twilio.rest import TwilioRestClient
from flask import Flask, request , make_response,render_template,redirect

from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

from reduction import *
from sentiment import *
import os

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
        updatedb(from_add,text)
        dataparser(sub, from_add, text)
        return make_response('',200)
    else:
        return "Bla"

def dataparser(sub, from_add, text):
    reduction = Reduction()
    reduction_ratio = 0.5
    parsed_list = reduction.reduce(text, reduction_ratio)
    parsed_text = ('').join(parsed_list)
    print(parsed_text)
    twil(sub, from_add, parsed_text)


def twil(sub,from_add,text):
    account_sid = "XXXXXXXXXXXXXXXXXXXX"   #get the XXXXXXXXXX stuff from your account
    auth_token = "XXXXXXXXXXXXXXXXX"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to="XXXXXXXXxX",from_="XXXXXXXXXXX",body="from:"+from_add+" subject:"+sub+" message:"+ text)

def updatedb(from_add,mes):
    usr=table.find_one(from_addr=from_add)
    if usr:
        usr['messages']=usr['messages'] + mes
        table.update(dict(from_addr=from_add, messages = usr['messages']),['from_addr'])
    else:
        table.insert(dict(from_addr=from_add, messages = mes))

def wordcloud(user):
    if os.path.exists('./static/cloud.png'):
        os.remove('./static/cloud.png')
    text = user['messages']
    tags = make_tags(get_tag_counts(text), maxsize=100)
    create_tag_image(tags, './static/cloud.png', size=(900, 600), fontname='Cuprum')

@app.route("/respond", methods=['GET', 'POST'])
def paid_respond():
    message = request.values.get('Body')
    message_elements = message.split(' ')
    resp = twilio.twiml.Response()
    if message_elements[0].lower() == 'wordcloud':
        message_elements.pop(0)
        addr = (' ').join(message_elements)
        usr = table.find_one(from_addr=addr)
        if usr:
             wordcloud(usr)
             resp.message("Image Generated XXXXXXXXXXXXXXXX/static/cloud.png") #replace XXXXXX with your server
        else:
            resp.message("Contact Not Found")
    else:
        resp.message("Invalid Syntax")
    return str(resp)

@app.route("/home", methods=['GET', 'POST'])
def view():
    if request.method == 'POST':
        usr = table.find_one(from_addr=request.form.get('user'))
        if usr:
            li = senti_analysis(usr['messages'])
            return render_template('line.html', lis=li)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8000,debug=True)
