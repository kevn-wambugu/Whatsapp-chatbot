from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Twily")
trainer = ListTrainer(chatbot)

# Train the chatbot based on the english corpus
# product names have to be unique and something a customer would type
#There's a limit for number of requests same link can receive
documentation_topics = (
    ("Niaje","Poa sana Nikusaidie aje Mzito"),
    ("Good Morning","Morning How May I Help You?"),
    ("Good Afternoon","Good Afternoon How May I Help You?"),
    ("Good Evening","Good Evening How May I Help You?"),
    ("Good Night","Good Night How May I Help You?"),
    ("hi", "Hello"),    
    ("hello", "Hello"), 
    ("name", "My name is Twily"),
    ("age", "I am a computer program"),
    ("your job", "I am a chatbot"),
    ("color", "I like blue"), 
    ("food", "I like pizza"),
    ("movie", "I like Star Wars"),
    ("book", "I like The Hobbit"),
    ("sport", "I like rugby"),
    ("sdk", "https://www.twilio.com/docs/sms/whatsapp#sdks"),
    ("twilio python helper library", "https://www.twilio.com/docs/libraries/python"),
    ("tutorials", "https://www.twilio.com/docs/sms/whatsapp/tutorial/send-and-receive-media-messages-twilio-api-whatsapp"),
    ("career","You can find more information here https://group.jumia.com/people/dream-job"),
    ("directors","You can find the faces of Jumia here https://group.jumia.com/people/faces-of-jumia"),
    ("news", "Jumia's Airtel Kenya partnership won't end delivery payment problems \n https://www.theafricareport.com/43387/jumias-airtel-kenya-partnership-wont-end-delivery-payment-problems \n Jumia launches Brands Festival campaign to promote authentic brands \n https://group.jumia.com/news/jumia-launches-brands-festival-campaign-to-promote-authentic-brands"),
    ("latest", "Find the latest news here https://group.jumia.com/press"),
    ("offers", "Enjoy sale with over 50% discount in Black Friday \n https://www.jumia.co.ke/mlp-black-friday/ \n Flash Sales \n https://www.jumia.co.ke/sp-flash-sales/"), 
    ("contact us", "Talk to us here https://group.jumia.com/contact"),
    ("about us", "Jumia is a leading Ecommerce platform in africa https://group.jumia.com/about-us")   
) 

twilio_knowledge = (
    ("Twilio description", "Simply put, Twilio is a developer platform for communications.\
        Software teams use Twilio APIs to add capabilities like voice, video, and messaging \
        to their applications. This enables businesses to provide the right communications \
        experience for their customers."),
    ("help me", "I can give you general information about this project"),
    ("Twilio email", "Sorry, you can submit a ticket at: https://www.twilio.com/console/support/tickets/create"),
    ("Twilio phone number", "We don't have a phone number for this type of account"),
    ("mailing address", "You can email our corporate headquaters at hello@jumia.co.ke "),
    ("chatterbot", "library making it easy to generate automated responses to a user's input, visit https://chatterbot.readthedocs.io/en/stable/"),
    ("textblob", "library for processing textual data, please visit https://textblob.readthedocs.io/en/dev/"),
    ("nltk", "library for processing textual data, please visit https://www.nltk.org/"),
    ("two methods payment", "Sorry, we only accept one payment method per order."),
    ("claim warranty", "Warranties are covered by Sellers and not by Jumia. You can claim any warranty by presenting the product and the Jumia invoice which serves as proof of purchase at an authorized service center. Do not hesitate to contact our Customer Service Call Center at 0700 000 990, 0711 011 011 or click on the following link and fill the form to be provided with the contact information of the service center of the Seller of your product."),
    ("right", "You can start by clicking on the category menu on the left side of the website, then select a category name that you prefer. This will show all the products we have in that category. Alternatively, if you know what you are looking for, just type the name of the product or brand in our search bar at the top of the page and click Search."),
    ("delivery charges", "Delivery charges are the costs undertaken by Jumia and our logistics partners to bring your ordered item(s) to your doorstep. This takes into consideration the size of the item(s) and your location."),
    ("account shop", "No, you don't need to have an account already created. You can create one on the spot, once you've found the product you want to buy. Alternatively you can log-in with your Facebook account."),
    ("pay order", "The Jumia mobile app and mobile website offers all the payment options that the Jumia website version offers. You can pay without any worries with the preferred option of your choice."),
    ("gift card", "Its simple! When you get to the payment stage while in checkout, simply enter the gift card code in the voucher box."),
    ("python", "Python is a programming language that is interpreted, object-oriented, and high-level."),
    ("pay", "You can choose from the different payment methods available on Jumia. Please find below the list of available payment methods: \n 1.Credit\n 2.Debit\n 3.Cash on Delivery\n 4.Pay on Delivery\n 5.Pay on Pickup\n 6.Pay on Pickup (Cash on Delivery)"),
    ("Card declined", "If you experience trouble completing payment through debit/credit card, first thing to do is to make sure that your card is activated for online payments and that you have enough funds/limit to complete the transaction. Your bank can help you verify these details."),
    ("hidden charges", "There are no hidden charges when you make a purchase on Jumia. The order amount is inclusive of all taxes and shipping fees. In case your order is delivered partially you will be required to pay only for the item that has been delivered to you. The order amount will be mentioned on the parcel and the invoice. Please note that we will never ask you to pay extra cash to the delivery."),
    ("pay Card","At the end of the checkout chose Credit / Debit Card as payment options and follow the steps after confirming your purchase. Make sure that your bank activated your Credit Card for online payments. Please note that Jumia provides the utmost security on your payments. Jumia has been operating in e-commerce in Africa since 2012, with a proven record for top security around the payments processed."),
    ("Tecno Spark 7", "https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/79/867434/1.jpg?5521 \n 64GB + 3GB RAM (Dual SIM) KSh 12,899 https://www.jumia.co.ke/spark-7-6.5-64gb-3gb-ram-dual-sim-5000mah-4gspruce-green-tecno-mpg307190.html"),
    ("Vitron HD 22", "https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/02/343943/1.jpg?9089 \n LED Digital TV -USB And HDMI CONNECTIVITY KSh 6,750 https://www.jumia.co.ke/hd-22-inchesled-digital-tv-usb-and-hdmi-connectivity-vitron-mpg302826.html"),
    ("mshipi","https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/65/352193/1.jpg?5034 \n Mens Buckle Leather Belt - BLACK KSh 460 https://www.jumia.co.ke/generic-mens-buckle-leather-belt-black-fashion-mpg318653.html"),
    ("Xiaomi redmi 9", "https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/95/060053/1.jpg?7517 \n 3GB 32GB 13.0MP Camera 4G LTE Smartphone - Sunset Purple KSh 11,499 https://www.jumia.co.ke/xiaomi-redmi-9-6.53-inch-3gb-32gb-13.0mp-camera-4g-lte-smartphone-sunset-purple-35006059.htmlmic-handsfree-rotation-28222753.html"),
    ("Huawei Y7 2019", "https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/97/930843/1.jpg?7995 \n 2GB RAM + 32GB (Dual SIM), 5500mAh, Black KSH 8,999 https://www.jumia.co.ke/note-10-6.52-2gb-ram-32gb-dual-sim-5500mah-black-ulefone-mpg324785.html"),
    ("LG woofer", "https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/59/632592/1.jpg?6933 \n Bluetooth,FM,USB-2.1 CH KSh 3,396 https://www.jumia.co.ke/sub-woofer-hometheatre-bluetoothfmusb-2.1-ch-amtec-mpg324825.html"),
    ("XIAOMI Smart Band 5", "https://ke.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/37/762613/1.jpg?0467 \n AMOLED Screen - Black, KSh 3,609 https://www.jumia.co.ke/xiaomi-mi-smart-band-5-amoled-screen-black-31626773.html")             
)
 
classifier = ("silly", "dumb", "stupid", "I'dont think so", "I don't care",
              "do you know anything", "not good", "omg", "this is not working"
              "this is bad", "not what I want", "live help",
              "get me a rep", "I need a real person", "forget you")


for topic, link in documentation_topics:
    trainer.train((
        f"{topic}",
        f"Sure, You can find more details here: {link}"
    ))

for topic, description in twilio_knowledge:
    trainer.train((
        f"{topic}",
        f"Ok sure, {description}"
    ))

for i in classifier:
    trainer.train((
        f"{i}",
        "I am sorry you feel that way, please ask the question again"
    ))

trainer.export_for_training('twilybot.json')