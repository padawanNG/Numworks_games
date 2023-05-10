from random import *
from kandinsky import fill_rect as f, draw_string as d
from ion import *
from time import monotonic
def create_boat(length):
  global grid,boat_coo
  rand=[randrange(0,8),randrange(0,8),randrange(0,2)]
  rand[rand[2]]=randrange(0,9-length)
  coo=[]
  for x in range(rand[0],rand[0]+rand[2]+length*(not rand[2])):
    for y in range(rand[1],rand[1]+(not rand[2])+length*(rand[2])):
      if grid[x][y]==1:
        for c in coo:
          grid[c[0]][c[1]]=0
        return 0
      else:
        grid[x][y]=1
        coo.append((x,y))
  boat_coo.append(coo)
def square(col):
  f(coo[0]*27,coo[1]*27,28,1,col)
  f(coo[0]*27,(coo[1]+1)*27,28,1,col)
  f(coo[0]*27,coo[1]*27+1,1,26,col)
  f((coo[0]+1)*27,coo[1]*27+1,1,26,col)
def cur(vx,vy):
  global t,coo
  if monotonic()-t>0.125:
    t=monotonic()
    square(COLORS[0])
    coo[0]=(coo[0]+vx)%8
    coo[1]=(coo[1]+vy)%8
    square(COLORS[3])
def cross(size,pos,col,length=0.1):
  length=int(size*0.1)
  for x in range(size-length+1):
    f(x+pos[0],pos[1]+x,length,length,col)
    f(x+pos[0],pos[1]+size-x,length,-length,col)
COLORS=(
(50,50,50),#backgroud
(75,115,153),#win
(220,170,80),#squares
(0,255,0))#cursor
t=monotonic()
coo=[0,0]
boat_coo=[]
bombs=24
score=0
f(0,0,320,222,COLORS[0])
f(0,0,216,216,COLORS[0])
for x in range(8):
  for y in range(8):
    f(x*27+1,y*27+1,26,26,COLORS[2])
d(str(bombs),220,0,COLORS[2],COLORS[0])
square(COLORS[3])
grid=[[0 for _ in range(8)]for _ in range(8)]
while len(boat_coo)<2:
  create_boat(2+len(boat_coo))
run=1
while run:
  if keydown(KEY_LEFT):
    cur(-1,0)
  elif keydown(KEY_UP):
    cur(0,-1)
  elif keydown(KEY_DOWN):
    cur(0,1)
  elif keydown(KEY_RIGHT):
    cur(1,0)
  elif keydown(KEY_OK) and grid[coo[0]][coo[1]]<2:
    f(coo[0]*27+1,coo[1]*27+1,26,26,COLORS[0])
    if grid[coo[0]][coo[1]]!=0:
      cross(26,[coo[0]*27+1,coo[1]*27+1],COLORS[1])
    grid[coo[0]][coo[1]]+=2
    bombs-=1
    f(220,0,50,20,COLORS[0])
    d(str(bombs),220,0,COLORS[2],COLORS[0])
    boat_found=0
    for boat_c in boat_coo:
      sq_found=0
      for c in boat_c:
        if grid[c[0]][c[1]]==3:
          sq_found+=1
      if sq_found==len(boat_c):
        for c in boat_c:
          cross(26,[c[0]*27+1,c[1]*27+1],COLORS[3])
        boat_found+=1
    if boat_found==len(boat_coo):
      d("you win !",80,100,COLORS[0],COLORS[2])
      run=0
    elif bombs==0:
      d("you lose !",80,100,COLORS[0],COLORS[2])
      run=0
