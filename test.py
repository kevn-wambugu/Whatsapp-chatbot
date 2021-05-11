import requests
from bs4 import BeautifulSoup
import pandas
import time
    
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept-Encoding": "*",
    "Connection": 'keep-alive'} 
  
  
data =[]
  
for i in range(1):
    url = "https://www.kilimall.co.ke/new/commoditysearch?c=1615&page=1"
    page = requests.get(url + str(i), headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    all = soup.find_all('div',attrs={"class":'.el-col.el-col-6'}) 
    for item in all:
        killmall = {}
        killmall["Title"]=item.find('div',attrs={"class":''}).get_text()
        killmall['Price']=item.find('div',attrs={"class":'wordwrap-box'}).get_text()
        data.append(killmall)
    print("DONE!")
    print(all)
    
print(data)