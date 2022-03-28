import pandas as pd
import requests
from bs4 import BeautifulSoup

res=requests.get("https://play.google.com/store/apps/category/GAME?hl=en_US&gl=US")
# print(res)

# content:
soup=BeautifulSoup(res.content,'html.parser')
# print(soup.prettify())

names= soup.find_all('div',class_="b8cIId ReQCgd KdSQre fmVS2c")
name=[]
for i in range(len(names)):
    name.append(names[i].get_text())
# print(name)

# images=soup.find_all('img',class_="T75of qxfgt")
# img=[]
# for i in range(len(images)):
#     img.append(images[i]['src'])
# print(img)

df=pd.DataFrame()
df["names"]=name

# print(df)
df.to_csv("app names.csv")






























