import  numpy as n 
#it splits only in equal number of elements.
a=n.arange(10,130,10)
print(n.split(a,2))#splits into 2 half
print(n.split(a,3))#splits into 3 hlaf
c=n.split(a,(2,5)) #it split upto 2 index and from 2 to 5-1=4 and then from 5 to end 
print(c)