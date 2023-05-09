# Credits to Numworks dev team
from math import *

def co(xa,ya,xb,yb):
  return xb-xa,yb-ya
  
def mid(xa,ya,xb,yb):
  return (xa+xb)/2,(ya+yb)/2

def colin(xab,yab,xcd,ycd):
  return xab*ycd-xcd*yab==0

def rect(xab,yab,xcd,ycd):
  return xab*xcd+ycd*yab==0
