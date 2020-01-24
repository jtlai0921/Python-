import requests
from bs4 import BeautifulSoup

urlstr='http://books.gotop.com.tw/default.aspx'
responseObj=requests.get(urlstr)
bs=BeautifulSoup(responseObj.text, 'html.parser')

print('標題：',bs.title.text)
#print(bs.select('#ctl00_labNews'))

data=bs.select('#ctl00_labNews')
linkText=data[0].find_all('a')

for n in range(0, len(linkText)):
    print(linkText[n].text)

