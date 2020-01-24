import time as T
timer = T.localtime()
year = timer.tm_year
moon = timer.tm_mon
day = timer.tm_mday
hour = timer.tm_hour
minu = timer.tm_min
sec = timer.tm_sec
print('%s-%s-%s %s:%s:%s' %(year,moon,day,hour,minu,sec))
