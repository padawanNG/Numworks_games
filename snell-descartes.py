# Coded by M-A G.  All rights reserved
import turtle
import math
from math import *
from turtle import *

print("Que cherches-tu ?")
print(" 1. i1  |  2. i2 ")
print(" 3. n1  |  4. n2 ")
p=int(input())

if p==1:
  print("Quelle est la valeur de n1 ?")
  a=float(input())
  print("Quelle est la valeur de i2 ?")
  b=radians(float(input()))
  print("Quelle est la valeur de n2")  
  c=float(input()) 
  k=degrees(asin(sin(b)*c/a))
  print("i1 mesure",k)
elif p==2:
  print("Quelle est la valeur de i1 ?")
  a=radians(float(input()))
  print("Quelle est la valeur de n1 ?")
  b=float(input())
  print("Quelle est la valeur de n2 ?")
  c=float(input())
  k=degrees(asin(sin(a)*b/c))
  print("i2 mesure",k)
elif p==3:
  print("Quelle est la valeur de n2 ?")
  a=float(input())
  print("Quelle est la valeur de i1 ?")
  b=radians(float(input()))
  print("Quelle est la valeur de i2 ?")
  c=radians(float(input()))
  k=a*sin(c)/sin(b)
  print("La valeur de n1 est",k)
elif p==4:
  print("Quelle est la valeur de i1")
  a=radians(float(input()))
  print("Quelle est la valeur de i2")
  b=radians(float(input()))
  print("Quelle est la valeur de n1")
  c=float(input()) 
  k=sin(a)*c/sin(b)
  print("La valeur de n2 est",k)
  
  # Coded by M-A G.  All rights reserved
