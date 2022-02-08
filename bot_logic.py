import pymongo


"""Function to get promotions and latest offers from the datatbase.
   The function creates a connenction to the mongodb database and finds three latest promotions.
   The results are stored in a string and that is what the functions returns. 
   The function is used by the flask application to send the message to the user
"""

def get_promotions():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    dataBase = client['project_bot']
    promotions = dataBase['promotions_offers']
    cursor = promotions.find({}, {"_id": 0, "name": 1, "link": 1 }).limit(3)

    result = []

    for data in cursor:
        result.append(data)
    if len(result) == 0:
        return "Sorry, we currently don't have any promotions"
        
    message = ""
    for data in result:
        message += f"{data['name']}\n"
        message += f"{data['link']}\n"
           
    message += '\n\n'

    return message


"""Function to get latest news from the datatbase.
   The function creates a connenction to the mongodb database and finds three latest news articles.
   It returns the title a brief description and a link to the article.
   The results are stored in a string and that is what the functions returns. 
   The function is used by the flask application to send the message to the user
"""

def get_news():
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    dataBase = client['project_bot']
    news = dataBase['news']
    cursor = news.find({}, { "_id": 0, "name": 1, "description": 1, "link":1}).limit(3)
    result = []

    for data in cursor:
        result.append(data)
        
    if len(result) == 0:
        return "Sorry, we currently don't have any news"
    message = ""
    for data in result:
        message += f"{data['name']}\n" 
        message += f"{data['description']}\n"
        message += f"{data['link']}\n"
        message += '\n\n\n'
        
    return message


"""Function to answer questions from users.
   The function creates a connenction to the mongodb database and matches the question with the response in the database.
   It returns the response in the database as the answer to the question by the user.
   The results are stored in a string and that is what the functions returns. 
   The function is used by the flask application to send the message response to the user.
"""

def answer_questions(question):
    client = pymongo.MongoClient('mongodb://localhost:27017/') 
    dataBase = client['project_bot']
    FAQ = dataBase['FAQ']
    query = { "Question": { "$regex": f"(?i){question}" }}
    cursor = FAQ.find(query)
    result = []
    for data in cursor:
        result.append(data)
    if len(result) == 0:
        return 'Hey! How may I help you?'
    message = ""
    for data in result:
        message += f"{data['response']}\n" 
                
    return message


"""Function to get products from the database.
   The function creates a connenction to the mongodb database and matches the product name to get prices link and image.
   The function has one argument,which is the name of the product the customer is serching for.
   The results are stored in a string and that is what the functions returns. 
   The function is used by the flask application to send the message to the user.
"""


def get_products(product_name):
    client = pymongo.MongoClient('mongodb://localhost:27017/') 
    dataBase = client['project_bot']
    products = dataBase['products']
    query = { "Name": { "$regex": f"(?i){product_name}" }}
    cursor = products.find(query)
    result = []
    for data in cursor:
        result.append(data)
    if len(result) == 0:
        return 'What are you are looking for?'
    message = ""
    get_products.image = ""
    for data in result:
        get_products.image += f"{data['image']}\n"
        message += f"{data['Name']}\n"
        message += f"{data['Price']}\n" 
        message += f"{data['link']}"
        
            
    return message