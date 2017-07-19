import time
from datetime import datetime 

# f = open('/home/aman/Desktop/some/output.txt','r')
# lines = f.readlines()
# t = lines[3]
# print t
# temp = t
# t = t.split(" ")
# t[-1] = t[-1][:len(temp)-1]
# t = " ".join(t)
# print t
# c = lines[2]
# c = c.split(" ")
# c[-1] = c[-1][:8]
# c = " ".join(c)
# print c
a = '10:50:00'
b = '10:40:00'
FMT = '%H:%M:%S'
tdelta = datetime.strptime(a, FMT) - datetime.strptime(b, FMT) 
print tdelta