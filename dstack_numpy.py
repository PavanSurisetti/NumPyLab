import numpy as n
a=n.arange(1,11).reshape(2,5)
b=n.arange(11,21).reshape(2,5)
print(a)
print('============')
print(b)
print('============')
c=n.dstack((a,b))
print(c)