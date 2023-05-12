from math import *
from ion import keydown
from kandinsky import fill_rect as drawRect, draw_string as drawTxt
from time import *
from random import randint,random
SCREEN_SIZE=(320,222)
LOGO=(29694911221719259620815,19)
NUMB=(31599,18740,29671,31207,18925,31183,31695,18727,31727,31215)
PARTY=(20266236847757577779063,19)
ENDED=(521406024322335892760215,20)
Mode,Diff,MaxPts,BallSpd,BallDetails,PadDetails,Col1,Col2,Col3,BgCol,Theme,Best=0,1,2,3,4,5,6,7,8,9,10,11
base_conf=[0,1,1,3,0,0,(255,255,255),(255,200,0),(100,100,100),(60,60,60),0,0]

def kd(x):
  if keydown(x):
    while keydown(x):pass
    return True
  return False

def menu(x,y,elements,col=(0,0,0),bg_col=(255,255,255)):
  kd(4)
  el_size,select,txt_size,draw=25,0,[0 for i in range(len(elements))],1
  def draw():
    for nb,el in enumerate(elements):
      drawRect(x,y+el_size*nb,10*txt_size[nb],el_size,bg_col)
      slcted=nb==select
      type=el[0]
      name=el[1]
      val=el[-1]
      if type=="btn":disp_txt=name
      if type=="sld":disp_txt=name+" : {}".format(val)
      if type=="lst":disp_txt=name+" : {}".format(el[2][val])
      if slcted: disp_txt="> "+disp_txt
      txt_size[nb]=len(disp_txt)
      drawTxt(disp_txt,x,y+nb*el_size,col,bg_col)
  draw()
  while True:
    if kd(1):
      select=max(0,select-1)
      draw()
    if kd(2):
      select=min(len(elements)-1,select+1)
      draw()
    if kd(0):
      type=elements[select][0]
      if type=="sld":elements[select][-1]=max(elements[select][-1]-1,elements[select][2][0])
      if type=="lst":elements[select][-1]=max(elements[select][-1]-1,0)
      draw()
    if kd(3):
      type=elements[select][0]
      if type=="sld":elements[select][-1]=min(elements[select][-1]+1,elements[select][2][1])
      if type=="lst":elements[select][-1]=min(elements[select][-1]+1,len(elements[select][2])-1)
      draw()
    if kd(4) and elements[select][0]=="btn":break
  return elements[select][1],{x[1]:x[-1] for x in elements if x[0]!="btn"}
  
def transition(conf=base_conf):
  saveConf(conf)
  """c=8
  for col in (conf[Col3],conf[BgCol]):
    for i in range(c-3,c+1):
      for x in range(0,SCREEN_SIZE[0],c):
        for y in range(0,SCREEN_SIZE[1],c):
          drawRect(x,y,i,i,col)
          drawRect(x+c//2,y+c//2,i,i,col)"""
  drawRect(0,0,320,222,conf[BgCol])

def resetMenu(conf):
  transition(conf)
  drawTxt("Reset the Game ?",10,10,conf[Col1],conf[BgCol])
  if menu(10,40,[["btn","Yes"],["btn","No"]],conf[Col1],conf[BgCol])[0]=="Yes":resetGame()
  else:return gameMenu,conf

def drawNuber(n,x,y,s,col):
  for i,j in enumerate(str(n)):
    drawSprite([NUMB[int(j)],3],x+s*4*i,y,s,col)

def drawSprite(sprite,x1,y1,s,col):
  img=sprite[0]
  row=sprite[1]
  for i in range(len(bin(img))-2):
    if img>>i & 1: drawRect(x1+(i%row)*s,y1+(i//row)*s,s,s,col)
    
def mainMenu(conf=base_conf):
  transition(conf)
  drawSprite(LOGO,10,10,12,conf[Col2])
  drawRect(10,80,300,142,conf[Col3])
  act_el=[["btn","Play"],["lst","Mode",("Solo","2 Player","Vs Comp."),conf[Mode]],["btn","Game Options"],["btn","Graphics Options"]]
  get_act=menu(20,100,act_el,conf[Col1],conf[Col3])
  conf[Mode]=get_act[1]["Mode"]
  if get_act[0]=="Game Options":return gameMenu,conf
  elif get_act[0]=="Graphics Options":return graphMenu,conf
  else:return gameEngine,conf

def gameMenu(conf=base_conf):
  transition(conf)
  drawTxt("GAME MENU",10,10,conf[Col2],conf[BgCol])
  drawRect(10,30,300,5,conf[Col3])
  act_el=[["sld","Max Points",(1,21),conf[MaxPts]],["sld","Ball Speed",(1,9),conf[BallSpd]],["sld","Difficulty",(1,10),conf[Diff]],["btn","Graphics Options"],["btn","Done"],["btn","Reset Game"]]
  get_act=menu(20,50,act_el,conf[Col1],conf[BgCol])
  conf[MaxPts]=get_act[1]["Max Points"]
  conf[BallSpd]=get_act[1]["Ball Speed"]
  conf[Diff]=get_act[1]["Difficulty"]
  if get_act[0]=="Done":return mainMenu,conf
  elif get_act[0]=="Reset Game":return resetMenu,conf
  else:return graphMenu,conf

def resetGame():
  conf=base_conf
  saveConf(conf)
  print("Game reset")
  return mainMenu,conf

def graphMenu(conf=base_conf):
  transition(conf)
  drawTxt("GRAPHICS MENU",10,10,conf[Col2],conf[BgCol])
  drawRect(10,30,300,5,conf[Col3])
  act_el=[["lst","Ball Details",("No","Yes"),conf[BallDetails]],["lst","Pad Details",("No","Yes"),conf[PadDetails]],["lst","Theme",("Dark","Light","Omega","NsiOs"),conf[Theme]],["btn","Game Options"],["btn","Done"],["btn","Apply"]]
  get_act=menu(20,50,act_el,conf[Col1],conf[BgCol])
  conf[BallDetails]=get_act[1]["Ball Details"]
  conf[PadDetails]=get_act[1]["Pad Details"]
  conf=setTheme(conf,get_act[1]["Theme"])
  if get_act[0]=="Done":return mainMenu,conf
  if get_act[0]=="Apply":return graphMenu,conf
  else:return gameMenu,conf

def setTheme(conf,nb):
  conf[Theme]=nb
  a,b,c,d=(255,255,255),(255,200,0),(100,100,100),(60,60,60)
  if nb==1:a,b,c,d=d,(200,150,60),(200,200,200),a
  elif nb==2:b=(220,50,50)
  elif nb==3:b=(200,100,200)
  conf[Col1:BgCol+1]=a,b,c,d
  return conf

def saveConf(conf):
  try :
    with open("pong.conf","w") as f:
      f.truncate(0)
      f.write(str(conf))
  except: print("Saving configuration failed.")

def loadConf():
  try:
    with open("pong.conf","r") as f:return eval(f.readline())
  except:
    print("Loading configuration failed.")
    return base_conf

def vec(s,a):
      a=radians(a)
      x=s*cos(a)
      y=s*sin(a)
      return x,y
def simp(a):return a%360
def collide(a1,a2):return a2-simp(a1-a2)
class Entity():
    def __init__(it,x,y,w,h,col,bg_col):
      it.x,it.y,it.w,it.h,it.col,it.bg_col=x,y,w,h,col,bg_col
      it.spd_x,it.spd_y=0,0
      it.last_draw=(int(it.x-it.w//2),int(it.y-it.h//2),int(it.w),int(it.h),it.bg_col)

    def hitBox(it,it2):
      if it.x-it.w//2<it2.x+it2.w//2 and it.x+it.w//2>it2.x-it2.w//2 and it.y-it.h//2<it2.y+it2.h//2 and it.x+it.w>it2.x and it.y<it2.y+it2.h//2 and it.y+it.h//2>it2.y-it2.h//2:return True
      else: return False

    def applyVec(it):
      it.x+=it.spd_x
      it.y+=it.spd_y
    def hideObj(it):drawRect(*it.last_draw)
    def drawObj(it,detail=0):
      it.last_draw=[int(it.x-it.w//2),int(it.y-it.h//2),int(it.w),int(it.h),it.bg_col]
      if detail:
        for x2,y2 in zip((2,0),(0,2)):drawRect(int(it.x-it.w//2)+x2,int(it.y-it.h//2)+y2,int(it.w)-x2*2,int(it.h)-y2*2,it.col)
      else: drawRect(*it.last_draw[0:4]+[it.col])
      
class Particule(Entity):
  def __init__(it,x,y,s,col,bg_col,spd,a):
    super().__init__(x,y,s,s,col,bg_col)
    it.spd_x,it.spd_y=vec(spd,simp(randint(-90,90)+a))
  def playFrame(it):
    it.hideObj()
    it.spd_y+=random()*4
    it.applyVec()
    it.drawObj()

def s(t):return monotonic()-t
def addParticules(nb,*part_info):
  lst=[]
  for i in range(nb):lst.append(Particule(*part_info))
  return lst

def gameEngine(conf=base_conf):
  def pause(conf):
    kd(8)
    drawTxt("Paused",SCREEN_SIZE[0]//2-30,SCREEN_SIZE[1]//2-10,conf[Col1],conf[BgCol])
    while not kd(8):pass
    drawRect(SCREEN_SIZE[0]//2-30,SCREEN_SIZE[1]//2-10,100,20,conf[BgCol])
  def error(n,t):return n*(randint(-t,t)/100+1)
  def resetScreen():drawRect(0,0,SCREEN_SIZE[0],SCREEN_SIZE[1],conf[BgCol])
  total_pts,pts,bounces,pad_size,ball_size,ball_spd,diff=0,[0,0],0,50,10,conf[BallSpd],conf[Diff]
  spf,targ_spf,frame_nb=monotonic(),0.016,0
  pad1,pad2=Entity(10,SCREEN_SIZE[1]//2,ball_size,pad_size,conf[Col1],conf[BgCol]),Entity(SCREEN_SIZE[0]-10,SCREEN_SIZE[1]//2,ball_size,pad_size,conf[Col1],conf[BgCol])
  ball=Entity(SCREEN_SIZE[0]//2,SCREEN_SIZE[1]//2,ball_size,ball_size,conf[Col2],conf[BgCol])
  line=Entity(SCREEN_SIZE[0]//2,SCREEN_SIZE[1]//2,ball_size,SCREEN_SIZE[1],conf[Col3],conf[BgCol])
  ball.a=0
  particules,delete=[],[]
  resetScreen()

  while total_pts<conf[MaxPts]:
    frame_nb+=1
    if frame_nb%5==0:
      line.drawObj()
      if conf[Mode]==0:drawNuber(bounces,10,10,10,conf[Col3])
      else:
        for x,n in zip((20,SCREEN_SIZE[0]//2+20),pts):drawNuber(n,x,10,10,conf[Col3])
    ball.drawObj(conf[BallDetails])
    for pad in (pad1,pad2):
      pad.hideObj()
      pad.drawObj(conf[PadDetails])
      pad.applyVec()
      pad.y=max(pad.h/2,min(SCREEN_SIZE[1]-pad.h/2,pad.y))
      pad.spd_y/=1.1
      if ball.hitBox(pad) and (pad1.x<ball.x<pad2.x):
        ball.a=collide(ball.a,simp(90-randint(-1,1)*diff)+10*(ball.y-pad.y)/pad.h)
        bounces+=1
        if conf[BallDetails]:particules+=addParticules(5,ball.x,ball.y,2,conf[Col2],conf[BgCol],20,ball.a)
        if conf[Mode]==0:drawRect(10,10,120,50,conf[BgCol])
        ball.x=pad.x-copysign(ball.w,pad.x-SCREEN_SIZE[0]//2)
    ball.spd_x,ball.spd_y=vec(ball_spd,ball.a)
    ball.a=simp(ball.a)
    ball.applyVec()
    if keydown(8):pause(conf)
    if keydown(1):pad1.spd_y-=1
    if keydown(2):pad1.spd_y+=1
    if conf[Mode]==0:
      pad2.y=pad1.y
    elif conf[Mode]==1:
      if keydown(39):pad2.spd_y-=1
      if keydown(45):pad2.spd_y+=1
    else:
      pad2.spd_y+=max(min(0.5,(error(ball.y,50-diff*2)-pad2.y)/10),-1)
    if ball.y-ball.h/2<=0 or ball.y+ball.h/2>=SCREEN_SIZE[1]:
      ball.a=collide(ball.a,0)
      if conf[BallDetails]:particules+=addParticules(5,ball.x,ball.y,2,conf[Col2],conf[BgCol],2,ball.a)
    if ball.x<0 or ball.x>SCREEN_SIZE[0]:
      resetScreen()
      if conf[BallDetails]:particules+=addParticules(20,ball.x,ball.y,2,conf[Col2],conf[BgCol],2,270)
      if conf[Mode]==0:break
      else:
        p=0 if ball.x>SCREEN_SIZE[0]//2 else 1
        pts[p]+=1
        total_pts+=1
      ball.x=SCREEN_SIZE[0]//2
    if frame_nb%4==0:
      for part in particules:
        part.playFrame()
        if part.y>=SCREEN_SIZE[1]:
          part.hideObj()
          delete.append(part)
      for i in delete:particules.remove(i)
      delete=[]
    while s(spf)<targ_spf:pass
    spf=monotonic()
    ball.hideObj()
    for pad in (pad1,pad2):pad.hideObj()
  if bounces>conf[Best]:conf[Best]=bounces
  return gameFinish(conf,pts,bounces)
  
def gameFinish(conf,pts,bounces):
  transition(conf)

  drawSprite(PARTY,90,10,8,conf[Col1])
  drawSprite(ENDED,125,50,4,conf[Col2])
  x,y=SCREEN_SIZE[0]//2,80
  if conf[Mode]==0:
    txt="Score: {} | Best: {}".format(bounces,conf[Best])
  else :
    if pts[0]==pts[1]:txt="Equality"
    elif pts[1]>pts[0]:
      if conf[Mode]==2:txt="Computer won"
      else:txt="Player 2 won"
    else:txt="Player 1 won"
    txt+=" | {}-{}".format(*pts)
  drawRect(0,80,SCREEN_SIZE[0],20,conf[Col3])
  drawTxt(txt,x-len(txt)*5,y,conf[Col1],conf[Col3])
  if menu(10,110,[("btn","Play Again"),("btn","Finish")],conf[Col1],conf[BgCol])[0]=="Play Again":return gameEngine,conf
  else:return mainMenu,conf

f,c=mainMenu,loadConf()
while 1:
  f,c=f(c)
