import numpy as n
a=n.arange(10,130,10)
print(n.searchsorted(a,10))#0
print(n.searchsorted(a,[90,100]))