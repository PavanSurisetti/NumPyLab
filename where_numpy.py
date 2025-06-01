import numpy as n
a=n.arange(10,130,10)
print(a)
print(n.where(a==80)) 
print(n.where(a%10==0))  
print(n.where(a>110))