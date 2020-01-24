import urllib
urlstr = 'http://books.gotop.com.tw/BookDetails.aspx?bn=AER048800'
parseResultObj = urllib.parse.urlparse(urlstr);

print('ParseResult物件資訊：',parseResultObj)
print('通訊埠號：',parseResultObj.port)
print('通訊協定：',parseResultObj.scheme)
print('網站位址：',parseResultObj.netloc)
print('網站路徑：',parseResultObj.path)
print('查詢字串：',parseResultObj.query)