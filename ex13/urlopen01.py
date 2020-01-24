import urllib.request
urlstr='http://books.gotop.com.tw/default.aspx'
responseObj=urllib.request.urlopen(urlstr)

print('網站網址：',responseObj.geturl())
print('讀取狀態：',responseObj.status)
print('網頁表頭：',responseObj.getheaders())
htmlContent=responseObj.read()
print('網頁資料：',htmlContent.decode())
