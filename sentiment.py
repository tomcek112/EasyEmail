import unirest

def senti_analysis(mess):
    li=[]
    messages = mess.split('.')
    for message in messages:
        response = unirest.get("https://loudelement-free-natural-language-processing-service.p.mashape.com/nlp-text/",headers={
    "X-Mashape-Key": "3dfTjCfvibmshu3jIzNWO6HD8cGBp1VrQrmjsn178rfmyCEKPe",
    "Accept": "application/json"},params = {"text":message})
        li.append(response.body['sentiment-score'])
    return li