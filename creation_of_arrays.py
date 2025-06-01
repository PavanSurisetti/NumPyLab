import numpy as n
a1=n.array([1,2,3])#1d
a0=n.array([1])#0d
a2=n.array([[1,2],[3,4]])#2d
a3=n.array([[[1,2,3],[4,5,6],[7,8,9]]])#3d
print(a0)
print(a1)
print(a2)
print(f'\n{a3},a3 dimension : {a3.ndim}')