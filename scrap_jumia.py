import requests
from bs4 import BeautifulSoup
import time
import pandas

headers = {
        "User-Agent": "Mozilla/5.100 (Windows NT .100; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/8100.100.3987.149 Safari/537.36",
        "Accept-Encoding": "*",
    "Connection": 'keep-alive'}


def scrap_from_jumia():

    lst=[]
    #Scrap from the phones_tablets category
    for i in range(1,100):

        url = "https://www.jumia.co.ke/phones-tablets/?page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"sku -gallery"})  
        for item in all:
            phones = {}
            phones["Title"]=item.find(attrs={"name"}).get_text()
            phones['Price']=item.find(attrs={"price"}).get_text()
            lst.append(phones)

        ds = soup.find_all('div',{'class':'sku -gallery -has-offers'})
        for item in ds:
            phones1 = {}
            phones1["Title"]=item.find(attrs={"name"}).get_text()
            phones1['Price']=item.find(attrs={"price"}).get_text()
            lst.append(phones1)
    print("DONE!")
    time.sleep(10)
    for i in range(1,100):

        url = "https://www.jumia.co.ke/electronics/?page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"sku -gallery"})  
        for item in all:
            electronics = {}
            electronics["Title"]=item.find(attrs={"name"}).get_text()
            electronics['Price']=item.find(attrs={"price"}).get_text()
            lst.append(electronics)

        ds=soup.find_all('div',{'class':'sku -gallery -has-offers'})
        for item in ds:
            electronics1 = {}
            electronics1["Title"]=item.find(attrs={"name"}).get_text()
            electronics1['Price']=item.find(attrs={"price"}).get_text()
            lst.append(electronics)
    print("DONE!")
    time.sleep(10)    
    for i in range(1,100):

        url = "https://www.jumia.co.ke/supermarket/?page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"sku -gallery"})  
        for item in all:
            supermarket = {}
            supermarket["Title"]=item.find(attrs={"name"}).get_text()
            supermarket['Price']=item.find(attrs={"price"}).get_text()
            lst.append(supermarket)
        ds=soup.find_all('div',{'class':'sku -gallery -has-offers'})
        for item in ds:
            supermarket1 = {}
            supermarket1["Title"]=item.find(attrs={"name"}).get_text()
            supermarket1['Price']=item.find(attrs={"price"}).get_text()
            lst.append(supermarket1)
    print("DONE!")
    time.sleep(10)
    for i in range(1,100):

        url = "https://www.jumia.co.ke/computing/?page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"sku -gallery"})  
        for item in all:
            computing = {}
            computing["Title"]=item.find(attrs={"name"}).get_text()
            computing['Price']=item.find(attrs={"price"}).get_text()
            computing['image']=item.find(attrs={"lazy image -loaded"}).get('image-src')
            lst.append(computing)
        ds = soup.find_all('div',{'class':'sku -gallery -has-offers'})
        for i in ds:
            computing1 = {}
            computing1["Title"]=item.find(attrs={"name"}).get_text()
            computing1['Price']=item.find(attrs={"price"}).get_text()
            lst.append(computing1)
    print("DONE!")
    time.sleep(10)
    for i in range(1,100):

        url = "https://www.jumia.co.ke/baby-products/?page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"sku -gallery"})  
        for item in all:
            baby = {}
            baby["Title"]=item.find(attrs={"name"}).get_text()
            baby['Price']=item.find(attrs={"price"}).get_text()
            lst.append(baby)
        ds = soup.find_all('div',{'class':'sku -gallery -has-offers'})
        for i in ds:
            baby1 = {}
            baby1["Title"]=item.find(attrs={"name"}).get_text()
            baby1['Price']=item.find(attrs={"price"}).get_text()
            lst.append(baby1)
    print("DONE!")
    time.sleep(10)
    for i in range(1,100):


        url = "https://www.jumia.co.ke/fashion/?page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"sku -gallery"})  
        for item in all:
            fashion = {}
            fashion["Title"]=item.find(attrs={"name"}).get_text()
            fashion['Price']=item.find(attrs={"price"}).get_text()
            lst.append(fashion)

        ds = soup.find_all('div',{'class':'sku -gallery -has-offers'})
        for i in ds:
            fashion1 = {}
            fashion1["Title"]=item.find(attrs={"name"}).get_text()
            fashion1['Price']=item.find(attrs={"price"}).get_text()
            lst.append(fashion1)
    print("DONE!")
    time.sleep(10)
    for i in range(1,100):

        url = "https://www.jumia.co.ke/health-beauty/?page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"sku -gallery"})  
        for item in all:
            beauty = {}
            beauty["Title"]=item.find(attrs={"name"}).get_text()
            beauty['Price']=item.find(attrs={"price"}).get_text()
            lst.append(beauty)
        ds = soup.find_all('div',{'class':'sku -gallery -has-offers'})
        for i in ds:
            beauty1 = {}
            beauty1["Title"]=item.find(attrs={"name"}).get_text()
            beauty1['Price']=item.find(attrs={"price"}).get_text()
            lst.append(beauty1)        
    print("DONE!")
    time.sleep(10)
    for i in range(1,100):
        url = "https://www.jumia.co.ke/home-office/?page=1"
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        all = soup.find_all('div',{'class':"sku -gallery"})  
        for item in all:
            office = {}
            office["Title"]=item.find(attrs={"name"}).get_text()
            office['Price']=item.find(attrs={"price"}).get_text()
            lst.append(office)
        ds = soup.find_all('div',{'class':'sku -gallery -has-offers'})
        for i in ds:
            office1 = {}
            office1["Title"]=item.find(attrs={"name"}).get_text()
            office1['Price']=item.find(attrs={"price"}).get_text()
            lst.append(office1)   

    print("DONE!")
    df = pandas.DataFrame(lst)
    df.to_csv("Jumia_data.csv")
    print("Scrapped Successfully!!!!")

scrap_from_jumia()