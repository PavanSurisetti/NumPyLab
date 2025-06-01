import numpy as n 
a=n.arange(10,110,10)
print(a.reshape(2,5))#manually done
b=a.reshape(5,-1)#automatically done
print(b)
print(b.flatten())#converts any array into 1-D array