# Credits to Numworks dev team
from math import *

def coordinates(x_A,y_A,x_B,y_B):
  return x_B-x_A,y_B-y_A
def collinear(x_1,y_1,x_2,y_2):
  return x_1*y_2-x_2*y_1==0
