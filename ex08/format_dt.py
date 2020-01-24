import datetime
d = datetime.datetime.now()
print('{:%Y-%m-%d %H:%M:%S}'.format(d))
print('{:%Y-%B-%d %A}'.format(d))
print('{:%x %X}'.format(d,d))
