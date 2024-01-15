#this code is for finding the local time at which the system is evoked based on time.ctime function
import time
seconds=1691243770.4344482
local_time=time.ctime(seconds)
print("local time:",local_time)
