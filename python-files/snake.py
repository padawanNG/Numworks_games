from random import *
from kandinsky import fill_rect as f, draw_string as d
from ion import *
from time import *
def add_cherry():
  cherry=(randrange(0,grid_size[0]),randrange(0,grid_size[1]))
  for c in body:
    if c==cherry:
      return add_cherry()
  return cherry
COLORS=(
(50,50,50),#background
(255,0,0),#cherry
(0,200,0),#snake body
(0,225,0),#snake head
(255,255,255))#text
body=[(0,0)]
add=4
dir=(1,0)
grid_size=(32,22)
size=10
tail=body[-1]
f(0,0,320,222,COLORS[0])
f(0,0,size,size,COLORS[2])
cherry=add_cherry()
f(cherry[0]*size,cherry[1]*size,size,size,COLORS[1])
t=monotonic()
run=1
while run:
  if monotonic()-t>1/10:
    t=monotonic()
    if keydown(KEY_UP) and dir[1]!=1:
      dir=(0,-1)
    elif keydown(KEY_LEFT) and dir[0]!=1:
      dir=(-1,0)
    elif keydown(KEY_DOWN) and dir[1]!=-1:
      dir=(0,1)
    elif keydown(KEY_RIGHT) and dir[0]!=-1:
      dir=(1,0)
    f(body[0][0]*size,body[0][1]*size,size,size,COLORS[2])
    tail=body[-1]
    for x in range(len(body)-1,0,-1):
      body[x]=body[x-1]
    body[0]=((body[0][0]+dir[0])%grid_size[0],(body[0][1]+dir[1])%grid_size[1])
    if add>0:
      body.append(tail)
      add-=1
    else:
      f(tail[0]*size,tail[1]*size,size,size,COLORS[0])
    if body[0]==cherry:
      add+=1
      cherry=add_cherry()
      f(cherry[0]*size,cherry[1]*size,size,size,COLORS[1])
    for x in range(1,len(body)):
      if body[x]==body[0]:
        d("You lost",0,0,COLORS[4],COLORS[0])
        run=0
    f(body[0][0]*size,body[0][1]*size,size,size,COLORS[3])
