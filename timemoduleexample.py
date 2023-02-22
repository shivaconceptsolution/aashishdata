import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
data=time.localtime(time.time())
print(data.tm_year,data.tm_mon)
