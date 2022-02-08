import re
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import simplebot as sb


app = Flask(__name__)
app.config['DEBUG'] = True
 

@app.route("/")
def home():
    return "<h2>Hello world</h2> Welcome to simplebot!"


@app.route("/get", methods=['POST'])
def get_bot_response():
    user_input = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    twily_response = sb.escalation(user_input)
    image = re.findall("^https", twily_response)
    if image:
        productDetails = twily_response.splitlines()
        msg.media(productDetails[0])
        msg.body(productDetails[1])   
    else:
        msg.body(twily_response)

    return str(resp)
    

@app.route("/test")
def bot_response():
    user_input = request.args.get('msg').lower()
    return f'<h2>{sb.escalation(user_input)}</h2> {sb.neg_distribution}'


if __name__ == "__main__":
    app.run()