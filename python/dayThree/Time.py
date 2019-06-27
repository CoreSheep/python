'''
1. get time
    i.  time() time stamp from 1970.1.1 00:00:00 to now
    ii. ctime()
    iii.gmtime()
2. strftime() and strptime()
3. time.perf_counter() and time.sleep() time of cpu clock
'''
import time

print(time.time())
print(time.ctime())

tm = time.gmtime()
print(tm)
print(time.strftime("%Y-%m-%d %B %a %H:%M:%S", tm)) # string ormat, struct_time

timestr = "2019.05.15 May Wed PM 03:34:55"
print(time.strptime(timestr, "%Y.%m.%d %B %a %p %H:%M:%S"))
#struct_time,  string format



