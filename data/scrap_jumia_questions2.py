import requests
from bs4 import BeautifulSoup
import pandas


"""This file scraps questions and responses from the Frequently asked questions page in https://www.jumia.co.ke/sp-faq/#menuanchor,
   Results are stored in a list and the data is eventually stored in a csv file.
   The script uses BeautifulSoup, requests and pandas to scrap make requests and store data into the csv file.
"""

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept-Encoding": "*",
    "Connection": 'keep-alive'} 
  
list = []

for i in range(1, 3):  
    url = "https://www.jumia.co.ke/sp-faq/#menuanchor"
    page = requests.get(url + str(i), headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    all = soup.find_all('div', {'class':"blcks"})  
    for item in all:
        data = {}
        data["Question"] = item.find(attrs={"menutitle"}).text.strip()
        data['response'] = item.find(attrs={"question"}).text.strip()
        list.append(data)

df = pandas.DataFrame(list)

df.to_csv("Jumia_data_questions2.csv")
print("Scrapped Successfully!!!!")
