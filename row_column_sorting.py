import numpy as  n 
a=n.array([[100,90,80],[70,60,50],[40,30,20]])
print('Before Sorting')
print(a)#before sort
print('After sorting')
print(n.sort(a,axis=0))#column sort
print(n.sort(a,axis=1))#row sort