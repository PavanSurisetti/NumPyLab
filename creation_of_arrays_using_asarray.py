import numpy as n
a1=n.asarray([1,2,3])
print(a1)
print(f'a1 dimension {a1.ndim}')
a2=n.asarray([[1,2],[3,4]])#2d
print(a2)
print(f'a2 dimension {a2.ndim}')
#using nditer for accessing a element by element..
print('---Using nditer() method---')
for i in n.nditer(a2):
    print(i)