import numpy as n
a=n.array([1,2,3])#original array
b=n.copy(a)#copy of a
c=b.view()#view of b
print('---Before Changing---')
print(f'a={a}')
print(f'b={b}')
print(f'c={c}')
a[0]=100
print('--After changing the original array--')
print(f'a={a}')
print(f'b={b}')
print(f'c={c}')
b[2]=200
print('--after changing the view original \"b\"--')
print(f'a={a}')
print(f'b={b}')
print(f'c={c}')