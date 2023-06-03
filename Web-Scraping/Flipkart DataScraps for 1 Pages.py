from bs4 import BeautifulSoup
import requests
import pandas as pd

flipkart = {}
Phone_Name = []
new_price = []
actual_price = []
delivery_status = []
feature = []
Image = []

link = 'https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=1'

response_code = requests.get(link)
html_text = response_code.content

soup = BeautifulSoup(html_text,'lxml')

phonez = soup.find_all('a','_1fQZEK')

for phone in phonez:
    name = phone.find('div','_4rR01T').get_text()
    sales_price = phone.find('div','_30jeq3 _1_WHN1').get_text()
    old_price = phone.find('div','_3I9_wc _27UcVY').get_text()
    
    features = phone.find('li','rgWa7D').get_text()
    img = phone.find('img','_396cs4')['src']
    Phone_Name.append(name)
    new_price.append(sales_price)
    actual_price.append(old_price)
    
    feature.append(features)
    Image.append(img)

flipkart['Phone Name']= Phone_Name
flipkart['Actual Price']= actual_price
flipkart['New Price']= new_price
flipkart['Features']= feature
flipkart['Images']= img

df = pd.DataFrame(flipkart,columns=['Phone Name','Actual Price', 'New Price', 'Features', 'Images'])
df.to_csv('Flipkart.csv')
print(df)