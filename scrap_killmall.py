import requests
from bs4 import BeautifulSoup
import pandas
import time
    
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept-Encoding": "*",
    "Connection": 'keep-alive'}
def scrap_from_killmall():
    data=[]
    #Health and Beauty
    for i in range(1,120):

        url = "1`"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"el-col el-col-6"})  
        for item in all:
            killmall = {}
            killmall["Title"]=item.find(attrs={"wordwrap"}).get_text()
            killmall['Price']=item.find(attrs={"wordwrap-price"}).get_text()
            data.append(killmall)
    print("DONE!")
    time.sleep(10)
    #Sports and outdoor   
    for i in range(1,120):

        url = "https://www.kilimall.co.ke/new/commoditysearch?c=1425&page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"el-col el-col-6"})  
        for item in all:
            killmall1 = {}
            killmall1["Title"]=item.find(attrs={"wordwrap"}).get_text()
            killmall1['Price']=item.find(attrs={"wordwrap-price"}).get_text()
            data.append(killmall1)
    print("DONE!")
    time.sleep(10)
    #Bags and Fashion
    for i in range(1,120):

        url = "https://www.kilimall.co.ke/new/commoditysearch?c=1385&page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"el-col el-col-6"})  
        for item in all:
            killmall2 = {}
            killmall2["Title"]=item.find(attrs={"wordwrap"}).get_text()
            killmall2['Price']=item.find(attrs={"wordwrap-price"}).get_text()
            data.append(killmall2)
    print("DONE!")
    time.sleep(10)
    #shoes
    for i in range(1,120):

        url = "https://www.kilimall.co.ke/new/commoditysearch?c=1350&page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"el-col el-col-6"})  
        for item in all:
            killmall3 = {}
            killmall3["Title"]=item.find(attrs={"wordwrap"}).get_text()
            killmall3['Price']=item.find(attrs={"wordwrap-price"}).get_text()
            data.append(killmall3)
    print("DONE!")
    time.sleep(10)

    #clothes
    for i in range(1,120):

        url = "https://www.kilimall.co.ke/new/commoditysearch?c=1294&page=2"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"el-col el-col-6"})  
        for item in all:
            killmall4 = {}
            killmall4["Title"]=item.find(attrs={"wordwrap"}).get_text()
            killmall4['Price']=item.find(attrs={"wordwrap-price"}).get_text()
            data.append(killmall4)

    print("DONE!")
    time.sleep(10)
    #home and living
    for i in range(1,120):

        url = "https://www.kilimall.co.ke/new/commoditysearch?c=1466&page=2"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"el-col el-col-6"})  
        for item in all:
            killmall5 = {}
            killmall5["Title"]=item.find(attrs={"wordwrap"}).get_text()
            killmall5['Price']=item.find(attrs={"wordwrap-price"}).get_text()
            data.append(killmall5)

    print("DONE!")
    time.sleep(10)        
    #computers and tablets
    for i in range(1,97):

        url = "https://www.kilimall.co.ke/new/commoditysearch?c=1072&page=2"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"el-col el-col-6"})  
        for item in all:
            killmall6 = {}
            killmall6["Title"]=item.find(attrs={"wordwrap"}).get_text()
            killmall6['Price']=item.find(attrs={"wordwrap-price"}).get_text()
            data.append(killmall6)

    print("DONE!")
    time.sleep(10)
    #electronics and appliances
    for i in range(1,120):

        url = "https://www.kilimall.co.ke/new/commoditysearch?c=1250&page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"el-col el-col-6"})  
        for item in all:
            killmall7 = {}
            killmall7["Title"]=item.find(attrs={"wordwrap"}).get_text()
            killmall7['Price']=item.find(attrs={"wordwrap-price"}).get_text()
            data.append(killmall7)
    print("DONE!")
    time.sleep(10)
    #baby products
    for i in range(1,120):
    
        url = "https://www.kilimall.co.ke/new/commoditysearch?c=1504&page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"el-col el-col-6"})  
        for item in all:
            killmall8 = {}
            killmall8["Title"]=item.find(attrs={"wordwrap"}).get_text()
            killmall8['Price']=item.find(attrs={"wordwrap-price"}).get_text()
            data.append(killmall8)
    print("DONE!")
    time.sleep(10)
    #automotive
    for i in range(1,85):
    
        url = "https://www.kilimall.co.ke/new/commoditysearch?c=1603&page=2"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"el-col el-col-6"})  
        for item in all:
            killmall9 = {}
            killmall9["Title"]=item.find(attrs={"wordwrap"}).get_text()
            killmall9['Price']=item.find(attrs={"wordwrap-price"}).get_text()
            data.append(killmall9)
    print("DONE!")
    time.sleep(10)
    for i in range(1,41):
        
        url = "https://www.kilimall.co.ke/new/commoditysearch?c=1563&page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"el-col el-col-6"})  
        for item in all:
            killmall10 = {}
            killmall10["Title"]=item.find(attrs={"wordwrap"}).get_text()
            killmall10['Price']=item.find(attrs={"wordwrap-price"}).get_text()
            data.append(killmall10)
    print("DONE!")

    frame = pandas.DataFrame(data)
    frame.to_csv("Killmall_data.csv")   
    print("Scrapped Successfully!!!!")


scrap_from_killmall()