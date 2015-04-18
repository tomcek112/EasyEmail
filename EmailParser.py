from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dataextract():
    if request.method =='POST':
        from_add = request.form['from']
        sub = request.form['subject']
        text = request.form['text']
        no_attch = request.form['attachments']
        dataparser(to_add,no_attch,sub,text)
        return 200

if __name__ == '__main__':
    app.run(debug=True)