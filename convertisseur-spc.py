# Coded by M-A G.  All rights reserved
from math import *

print("Convertir de...")
print(" 1. femto  |  15. peta")
print(" 2. pico   |  14. tera")
print(" 3. nano   |  13. giga")
print(" 4. micro  |  12. mega")
print(" 5. milli  |  11. kilo")
print(" 6. centi  |  10. hecto")
print(" 7. deci   |   9. deca")
print("       8. normal     ")

j=int(input())

print("Vers...")
print(" 1. femto  |  15. peta")
print(" 2. pico   |  14. tera")
print(" 3. nano   |  13. giga")
print(" 4. micro  |  12. mega")
print(" 5. milli  |  11. kilo")
print(" 6. centi  |  10. hecto")
print(" 7. deci   |   9. deca")
print("       8. normal     ")

i=int(input())

print("Valeur a convertir...")
k=float(input())
  
def bip(a):
  
  if 12>a>4:
    a-=8
  elif a==14: 
    a-=2
  elif a==13:
    a-=4
  elif a==12:
    a-=6
  elif a==4:
    a-=10
  elif a==3:
    a-=12
  elif a==2:
    a-=14
  elif a==1:
    a-=16
  return a 
c=bip(j)
d=bip(i)

if j<i:
  l=c-d        
  f=k*10**l
if j>i:
  l=d-c
  f=k*10**(-l)
        
print("Cela donne",f)

# Coded by M-A G.  All rights reserved
