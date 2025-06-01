import numpy as n
a=n.array([1,2,3])#1d
print(f'before appending:{a}')
a=n.append(a,[4,5])
print(f'after appending:{a}')#1d
b=n.array([[1,2],[3,4]])
c=n.array([[5,6],[7,8]])
print('appending multidimensional arrays')
print(n.append(b,c))
