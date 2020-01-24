import requests
urlstr='http://books.gotop.com.tw/default.aspx'

responseObj=requests.get(urlstr)

print('網站網址：',responseObj.url)
print('讀取狀態：',responseObj.status_code)
print('網頁表頭：',responseObj.headers)
responseObj.encoding='utf-8'
print('網頁資料：',responseObj.text)
