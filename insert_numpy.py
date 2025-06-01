import numpy as n
a=n.arange(1,10,2)
print(f'before inserting :{a}')
a=n.insert(a,1,[2])
print(f'after inserting :{a}')
