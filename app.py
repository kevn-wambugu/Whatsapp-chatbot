from flask import Flask,request
import requests
from twilio.twiml.messaging_response import MessagingResponse 
import pymysql
import time

app = Flask(__name__)

@app.route("/bot",methods=["POST"])

def bot():
    incomin_msg = request.values.get("Body","").lower()
    response = MessagingResponse()
    msg = response.message()
    responded = False

    def get_jumia():
        conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="python_app")
        cur = conn.cursor()
        cur.execute("SELECT title,price FROM jumia_data WHERE title LIKE %s " , ("%" + incomin_msg + '%',))
        result = cur.fetchall()
        for row in result:
            #msg.media(row[4])
            msg.body(str(row[0:2]).replace("(", " " ).replace(")"," ").replace("'"," ") + "\n")
            responded = True
            
    """def get_killmall():
        conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="python_app")
        cur = conn.cursor()
        cur.execute("SELECT title,price FROM killmall_data WHERE title LIKE %s " , ("%" + incomin_msg + '%',))
        result = cur.fetchall()
        for row in result:
            #msg.media(row[4])
            msg.body(str(row[0:2]).replace("(", " " ).replace(")"," ").replace("'"," ") + "\n")
            responded = True """

    get_jumia()
    time.sleep(5)
   
    if not responded:
        msg.body('Unable to return data right now! ')
    
    return str(response)


if __name__ == '__main__':
    app.run()
