import numpy as n
a=n.arange(1,11)
b=n.arange(11,21)
print(a)
print(b)
print(n.equal(a,b))#element wise
print(n.not_equal(a,b))
print(n.less(a,b))
print(n.greater(a,b))
print(n.less_equal(a,b))
print(n.greater_equal(a,b))