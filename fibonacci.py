from math import *

kk = []

x=1
y=1

for i in range(15):
  x+=y
  kk.append(x)
  y+=x
  kk.append(y)
print(kk)
