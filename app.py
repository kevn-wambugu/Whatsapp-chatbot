from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse 
from bot_logic import *

app = Flask(__name__)

@app.route("/bot", methods=["POST"])


def bot():
    incoming_msg = request.values.get("Body", "").strip().lower()
    response = MessagingResponse()
    msg = response.message()
    responded = False
    
    if 'hello' in incoming_msg:
        mainmenu = ("Hello  \n How may I help you?\n 1. Check products\n 2. Customer support\n 3.See promotions\n 4. Latest news\n Please pick a number")
        msg.body(mainmenu)
        
    if '1' in incoming_msg:
        product = get_products(incoming_msg)
        msg.media(get_products.image)
        msg.body(product)
      
    if '2' in incoming_msg:
        question = answer_questions(incoming_msg)
        response.message(question)

    if '3' in incoming_msg:
        promotions = get_promotions()
        response.message(promotions) 

    if '4' in incoming_msg:
        news = get_news()
        response.message(news)
     
    return str(response)
       
if __name__ == '__main__':
    app.run(debug=True)
