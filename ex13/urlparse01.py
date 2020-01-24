import urllib
urlstr = 'http://books.gotop.com.tw/BookDetails.aspx?bn=AER048800'
resultObj = urllib.parse.urlparse(urlstr);

print('ParseResult物件資訊：',resultObj)
print('通訊埠號：',resultObj.port)
print('通訊協定：',resultObj.scheme)
print('網站位址：',resultObj.netloc)
print('網站路徑：',resultObj.path)
print('查詢字串：',resultObj.query)