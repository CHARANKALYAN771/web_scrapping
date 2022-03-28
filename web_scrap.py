import pandas as pd
import requests
from bs4 import BeautifulSoup
response=requests.get('https://www.flipkart.com/search?q=fridge%20double%20door%20fridge%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
# print(response)

soup=BeautifulSoup(response.content,'html.parser')
# print(soup.prettify())

names= soup.find_all('div',class_="_4rR01T")
name=[]
for i in range(len(names)):
    name.append(names[i].get_text())
# print(name)

images=soup.find_all('img',class_="_396cs4 _3exPp9")
img=[]
for i in range(len(images)):
    img.append(images[i]['src'])
# print(img)

costs=soup.find_all('div',class_="_30jeq3 _1_WHN1")
cost=[]
for i in range(len(costs)):
    cost.append(costs[i].get_text())
# print(cost)

rats=soup.find_all('div',class_="_3LWZlK")
rat=[]
for i in range(len(rats)):
    rat.append(rats[i].get_text())
# print(rat)
ra=[]
for i in range(0,24):
    ra.append(rat[i])

links=soup.find_all('a',class_="_1fQZEK")
link=[]
for i in range(len(links)):
    s ='https://www.flipkart.com' + links[i]['href']
    link.append(s)
# print(link)

# df=pd.DataFrame()
# df['name']=name
# df['cost']=cost
# df['ratings']=rat
# df['images']=img
# df['links']=link

df=pd.DataFrame()
df['Name']=name
df['Price']=cost
df['ratings']=ra
df['Images']=img
df['Links']=link

# print(df)

df.to_csv('flipkart.csv',index=True)


























