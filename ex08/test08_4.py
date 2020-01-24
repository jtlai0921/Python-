import datetime
dt = datetime.datetime(2019,1,1,12,0)
print('{:%b-%d-%y %H:%M}'.format(dt))
f = 9876543.210
print('{1:,.4f}'.format(dt,f))
