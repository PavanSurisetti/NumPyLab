import numpy as n
temp=b'Hello Ganesha'
a1=n.frombuffer(temp,dtype='S1',count=6,offset=6)#for string representing them S1
print(a1)