from kandinsky import fill_rect, draw_string 
from random import choice
from time import sleep
from ion import *

v = [0]*16
s = [1]*16
end = 4
chiffres = [31599,18724,29671,31207,18925,31183,31695,18727,31727,31215]
sco = 0

def aff(n,x,y):
  if n>0:
    for k,c in enumerate(str(n)):
      for i in range(16):
        if chiffres[int(c)]>>i & 1 == 1:
          fill_rect(x+12*k+(i%3)*3,y+(i//3)*3,3,3,(110,110,90))
        
def ajout():
  global end
  vides = [i for i,x in enumerate(v) if x==0]
  if len(vides) != 0:
    end = 4
    v[choice(vides)] = choice([2,2,2,4])
  else:
    end -= 1
  plateau()
  
def gauche(r):
  return ([x for x in r if x!=0]+[0]*4)[:4]

def simp(r):
  global sco
  r = gauche(r)
  for i in range(1,4):
    if r[i] == r[i-1]:
      r[i-1] *= 2
      r[i] = 0
      sco += r[i-1]
  return gauche(r)    

def calcul(ligne,pas):
  global s
  s=list(v)
  for i in range(4):
    pos = simp([v[ligne[k]+pas*i] for k in range(4)])
    for k in range(4):
      v[ligne[k]+pas*i] = pos[k]
  ajout()
          
def plateau():
  global sco
  for i in range(16):
    if s[i]!=v[i]:
      g = max(0,int(-v[i]/2+255))
      fill_rect(64+50*(i%4),3+50*(i//4),47,47,(g,g,g))
      aff(v[i],66+50*(i%4)+24-6*len(str(v[i])),20+50*(i//4))
  draw_string(("0000"+str(sco))[-5:],266,205,(255,255,255),(255,181,49))

def game_over():
  fill_rect(102,90,120,25,(197,52,49)) # Omega's colors
  draw_string(" Game Over",110,94,(255,255,255),(197,52,49))
    
def go():
  global end
  fill_rect(62,1,203,203,(190,170,160))
  ajout()
  while end !=0 :
    if keydown(KEY_LEFT): calcul([0,1,2,3],4)
    elif keydown(KEY_RIGHT): calcul([3,2,1,0],4)
    elif keydown(KEY_UP): calcul([0,4,8,12],1)
    elif keydown(KEY_DOWN): calcul([12,8,4,0],1)
    sleep(.142)
  game_over()

go()
