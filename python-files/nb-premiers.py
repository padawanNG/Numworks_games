# Coded by M-A G.  All rights reserved
from math import *

print('')
print("==============================================")
print(" Bienvenue sur le programme des nbrs premiers ")
print("==============================================")
print('')

o=int(input("De : "))
j=int(input("À : "))
nb_premiers=[]

dernier=o

def testation(a):
  divs=[]
  i=1
  u=sqrt(a)
  uu=floor(u) 
  for k in range(uu):
    if a%i==0:
      divs.append(i)
    i+=1
  divs.append(a)    
  if divs[1]==a:
    nb_premiers.append(a)
      
liste=[]
for p in range(j-o):
  liste.append(o)
  o+=1

if liste[0]==0:
  liste.remove(0)
  liste.remove(1)

for nb in liste:
  testation(nb)

testation(j)  
print(nb_premiers)

print('')
print("==================")
print(" Fin du programme ")
print("==================")

# Coded by M-A G.  All rights reserved
