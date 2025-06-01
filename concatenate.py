import numpy as n
a=n.arange(1,11).reshape(2,-1)
b=n.arange(11,21).reshape(2,-1)
print(a)
print()
print(b)
print()
print(n.concatenate((a,b)))#general concatenate
print()
print(n.concatenate((a,b),axis=0))#col wise
print()
print(n.concatenate((a,b),axis=1))#row wise
