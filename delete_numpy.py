import numpy as n
a=n.arange(1,10)
print(f'before deleting:{a}')
a=n.delete(a,2)
print(f'after deleting:{a}')
b=n.arange(1,11).reshape(2,-1)
print(b)
b=n.delete(b,1)
print(b)