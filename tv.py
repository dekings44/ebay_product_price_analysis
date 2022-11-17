#importing the libraries needed 
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


#Declaring the headers 
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

#declaring the list of empty variables, So that we can append the data overall

phone_name = []
phone_state = []
phone_price =[]


#creating an array of values and passing it in the url for dynamic webpages
pages = np.arange(1,50,1)

#the whole core of the script
for page in pages:
    page = requests.get("https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw=mobile+phones&_sacat=15032&_ipg=240&rt=nc&_pgn="+str(page))
    soup = BeautifulSoup(page.text, 'html.parser')
    acc_data = soup.find_all('div', {'class': 's-item__info clearfix'})
    sleep(randint(2,6))
    # print(acc_data[0])
    for store in acc_data:
        name = store.find('div', {'class' : 's-item__title'}).text
        phone_name.append(name)
        
        state = store.find('span', {'class' : 'SECONDARY_INFO'}).text
        phone_state.append(state)
        
        price = store.find('span', {'class' : 's-item__price'}).text
        phone_price.append(price)

data = pd.DataFrame({"TV detail": phone_name, "TV State" : phone_state, "TV Price": phone_price})

print(data.head())

data.to_csv('ebay_phones.csv', index = None)