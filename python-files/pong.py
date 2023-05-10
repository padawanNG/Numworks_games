from math import cos,sin,pi
from kandinsky import *
from ion import *
from random import random,randint
#menu
def menu():
  global vitesse,Vraquette
  draw_string("Mode",140,20,'orange')
  draw_string("1 joueur    2 joueurs",60,40,'orange')
  mode=1
  while not (keydown(KEY_OK) or keydown(KEY_EXE)):
    draw_string("[",40+120*mode,40,'blue')
    draw_string("]",150+130*mode,40,'blue')
    if keydown(KEY_LEFT) or keydown(KEY_RIGHT):
      mode=1-mode
      draw_string(" ",40+120*(1-mode),40)
      draw_string(" ",150+130*(1-mode),40)
      while keydown(KEY_LEFT) or keydown(KEY_RIGHT):True
  while keydown(KEY_OK) or keydown(KEY_EXE):True
  draw_string("Vitesse du jeu",90,70,'orange')
  draw_string("lent   moyen   rapide",60,90,'orange')
  vitesse=2
  while not (keydown(KEY_OK) or keydown(KEY_EXE)):
    draw_string("[",-30+70*vitesse+10*(vitesse//3),90,'blue')
    draw_string("]",30+80*vitesse+10*(vitesse//3),90,'blue')
    dv=keydown(KEY_RIGHT)-keydown(KEY_LEFT)
    if (keydown(KEY_RIGHT) or keydown(KEY_LEFT)) and dv != 0:
      draw_string(" ",-30+70*vitesse+10*(vitesse//3),90)
      draw_string(" ",30+80*vitesse+10*(vitesse//3),90)
      vitesse=(vitesse+dv-1)%3+1
      while keydown(KEY_RIGHT) or keydown(KEY_LEFT):True
  while keydown(KEY_OK) or keydown(KEY_EXE):True
  draw_string("Déplacement des raquettes",55,120,'orange')
  draw_string("lent   moyen   rapide",60,140,'orange')
  Vraquette=2
  while not (keydown(KEY_OK) or keydown(KEY_EXE)):
    draw_string("[",-30+70*Vraquette+10*(Vraquette//3),140,'blue')
    draw_string("]",30+80*Vraquette+10*(Vraquette//3),140,'blue')
    dr=keydown(KEY_RIGHT)-keydown(KEY_LEFT)
    if (keydown(KEY_RIGHT) or keydown(KEY_LEFT)) and dr != 0:
      draw_string(" ",-30+70*Vraquette+10*(Vraquette//3),140)
      draw_string(" ",30+80*Vraquette+10*(Vraquette//3),140)
      Vraquette=(Vraquette+dr-1)%3+1
      while keydown(KEY_RIGHT) or keydown(KEY_LEFT):True
  # ajouter mode de rebond : angle relatif ou absolu
  return mode
mode=menu()
fill_rect(0,18,320,1,'purple')
fill_rect(0,204,320,1,'purple')
#raquette 1
x1=5
y1=111

#raquette 2
x2=315
y2=111

#balle
x=160
y=111

def balle(x,y,couleur):
  fill_rect(x-2,y-2,5,5,couleur)

def raquette(x,y,couleur):
  fill_rect(x-1,y-10,3,21,couleur)

score=[0,0]
angle=(pi/6-pi/18)*random()+pi/18
horiz=2*randint(0,1)-1
verti=1
clr1,clr2=(96,44,120),(104,44,128)
while 1:
  fill_rect(0,19,320,185,'white')
  x,y=160,111
  x1,y1=5,111
  x2,y2=315,111
  #vitesse=2
  V=vitesse
  while 1:
    d1 = (keydown(KEY_DOWN)-keydown(KEY_UP))
    y1 = max(min(193,y1+(vitesse+Vraquette-1)*d1),29) # y1 +=3*d1
    if mode:
      d2 = (keydown(KEY_RIGHT)-keydown(KEY_LEFT))
    else:
      d2 = min(vitesse+Vraquette-1,abs(int(y2-y)))*(2*(y>y2)-1)
    y2 = max(min(193,y2+d2*(1+(vitesse+Vraquette-1-1)*mode)),29)#y2 += d2 #3*(2*randint(0,3)-3
    #draw_string("|",x1,y1,['green','red'][(y1-y)**2>100])
    raquette(x1,y1,['green','red'][(y1-y)**2>169])
    if d1 != 0:fill_rect(x1-1,y1-2-13*d1,5,5,'white')
    raquette(x2,y2,['blue','red'][(y2-y)**2>169])
    if d2 != 0:
      if mode:
        fill_rect(x2-1,y2-2-13*d2,5,5,'white')
      else:
        fill_rect(x2-1,y2-2-13*(2*(y>y2)-1),5,5,'white')

    vx=x
    vy=y
    balle(int(x),int(y),"white")
    x+=V*cos(angle)*horiz
    y+=V*sin(angle)*verti
    clr1,clr2=clr2,clr1
    balle(int(x),int(y),clr1)
    for i in range(5):
      for j in range(5):
        if get_pixel(int(vx)-2+i,int(vy)-2+j)==clr2:
          set_pixel(int(vx)-2+i,int(vy)-2+j,'white')
    
    if x>311:
      horiz = -1
      if (y-y2)**2>169:
        draw_string("Joueur1 a gagné",85,110)
        score[0]+=1
        break
      else:
        #angle=min(2*pi/5,angle+(y-y2)*pi/180)
        angle=abs(6*(y-y2)*pi/180)
        verti = 2*(y>y2)-1
        V *= 1.1
        draw_string("Vitesse : "+str(V)[:4]+"  ",15,205,'blue')
        draw_string("Angle : "+str(int(abs(angle*180/pi)))+"°  ",180,205,'green')
    if x<9:
      horiz = 1
      if (y-y1)**2>169:
        draw_string("Joueur2 a gagné",85,110)
        score[1]+=1
        break
      else:
        #angle=min(2*pi/5,angle+(y-y1)*pi/180)
        angle=abs(6*(y-y1)*pi/180)
        verti = 2*(y>y1)-1
        V *= 1.1
        draw_string("Vitesse : "+str(V)[:4]+"  ",15,205,'blue')
        draw_string("Angle : "+str(int(abs(angle*180/pi)))+"°  ",180,205,'green')
    if y>200 or y<22:
      verti *= -1
      #angle *= -1
    fill_rect(0,204,320,1,'purple')
    fill_rect(0,18,320,1,'purple')
  while not keydown(KEY_EXE):
    draw_string("Score : "+str(score[0])+" - "+str(score[1]),60,0,'red')
    draw_string("EXE",145,131,'purple','cyan')
