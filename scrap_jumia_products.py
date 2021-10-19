import requests
from bs4 import BeautifulSoup
import pandas


"""This file scraps product name, image, price and a link from Jumia.co.ke,
   Results are stored in a list and the data is eventually stored in a csv file.
   The script uses BeautifulSoup, requests and pandas to scrap make requests and store data into the csv file.
"""

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept-Encoding": "*",
    "Connection": 'keep-alive'} 
  
list = []

for i in range(1, 3):  
    url = "https://www.jumia.co.ke/?page=4"
    page = requests.get(url + str(i), headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    all = soup.find_all('div', {'class':"itm col"})  
    for item in all:
        data = {}
        data["Name"] = item.find(attrs={"name"}).text.strip()
        data['Price'] = item.find(attrs={"prc"}).text.strip()
        data['image'] = item.find('img').get('data-src')

        domain = "https://www.jumia.co.ke" + item.a['href']

        data['link'] = domain
        list.append(data)

df = pandas.DataFrame(list)
df.to_csv("Jumia_data.csv")
print("Scrapped Successfully!!!!")
