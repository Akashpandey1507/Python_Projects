from bs4 import BeautifulSoup
import requests
import pandas as pd

Flipkart_Data = {}
Product_Name = []
Price = []
Description = []
Rating = []
Delivery = []

for i in range(1,21):

    url = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i)

    response_code = requests.get(url)

    soup = BeautifulSoup(response_code.text,'lxml')
    box = soup.find('div',class_='_1YokD2 _3Mn1Gg')

    name = box.find_all('div',class_ = '_4rR01T')
    for i in name:
        Product_Name.append(i.text)

    price = box.find_all('div', class_ = '_30jeq3 _1_WHN1')
    for p in price:
        Price.append(p.text)

    des = box.find_all('ul',class_='_1xgFaf')
    for d in des:
        Description.append(d.text)


Flipkart_Data['Product Name'] = Product_Name
Flipkart_Data['Product Price'] = Price
Flipkart_Data['Descriptions'] = Description



df = pd.DataFrame(Flipkart_Data)

print(df)
    
df.to_csv('Laptop.csv')

