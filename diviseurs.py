from math import *

j=int(input("Quel nombre:"))

divs=[]
i=1
for k in range(j):
  if j%i==0:
    divs.append(i)
  i+=1  
print(divs)    

if divs[1]==j:
  print(j,"est premier !!!")
