from kandinsky import fill_rect as f, draw_string as d
from ion import *
from time import monotonic
gr_p=(
#pawn
((10,6,3),(9,7,5),(9,8,5),(9,9,5),(10,10,3),(10,13,3),(9,14,5),(8,15,7),(8,16,7),(8,17,7),(7,18,9),(5,19,13),(4,20,15),(4,21,15),(4,22,15)),
#knight
((8,0,2),(8,1,3),(7,2,7),(6,3,10),(6,4,11),(5,5,13),(5,6,14),(4,7,15),(4,8,16),(3,9,18),(2,10,9),(12,10,9),(2,11,7),(11,11,10),(2,12,5),(11,12,10),(3,13,3),(10,13,11),(9,14,12),(8,15,13),(7,16,14),(7,17,13),(7,18,13),(6,19,15),(5,20,16),(5,21,16),(5,22,16)),
#bishop
((10,0,3),(9,1,5),(9,2,5),(10,3,3),(9,4,3),(14,4,1),(8,5,4),(13,5,3),(7,6,4),(13,6,4),(6,7,5),(13,7,4),(6,8,5),(12,8,6),(5,9,6),(12,9,6),(5,10,13),(5,11,12),(6,12,11),(6,13,11),(7,14,9),(8,16,8),(7,17,10),(0,18,23),(0,19,23),(0,20,11),(12,20,11),(1,21,9),(13,21,10),(1,22,8),(14,22,8)),
#rook
((9,0,5),(3,1,4),(9,1,5),(16,1,4),(3,2,4),(9,2,5),(16,2,4),(3,3,5),(9,3,5),(15,3,5),(3,4,17),(3,5,17),(4,6,15),(4,7,15),(5,8,13),(5,9,13),(5,10,13),(5,11,13),(5,12,13),(5,13,13),(4,14,15),(4,15,15),(4,16,15),(4,17,15),(3,18,17),(2,19,19),(2,20,19),(2,21,19),(2,22,19)),
#queen
((10,0,3),(9,1,5),(9,2,5),(1,3,3),(9,3,5),(19,3,3),(0,4,5),(10,4,3),(18,4,5),(0,5,5),(11,5,1),(18,5,5),(0,6,5),(11,6,1),(18,6,5),(1,7,3),(10,7,3),(19,7,3),(3,8,2),(10,8,3),(18,8,2),(4,9,2),(10,9,3),(17,9,2),(4,10,4),(10,10,3),(15,10,4),(5,11,13),(5,12,13),(5,13,13),(6,14,11),(6,15,11),(7,16,9),(7,17,9),(7,18,9),(6,19,11),(3,20,17),(2,21,19),(2,22,19)),
#king
((10,0,3),(9,1,5),(9,2,5),(10,3,3),(11,4,1),(3,5,5),(11,5,1),(15,5,5),(2,6,7),(10,6,3),(14,6,7),(1,7,21),(0,8,23),(0,9,23),(0,10,5),(7,10,9),(18,10,5),(0,11,5),(8,11,7),(18,11,5),(0,12,6),(8,12,7),(17,12,6),(1,13,6),(8,13,7),(16,13,6),(2,14,19),(3,15,17),(4,16,15),(5,17,13),(5,18,13),(4,19,15),(3,20,17),(2,21,19),(2,22,19)))
def c_g(pos_str):
  grid=[[[-1,-1]for _ in range(8)]for _ in range(8)]
  a=0
  for c in pos_str:
    try:
      a+=int(c)
    except ValueError:
      grid[a%8][a//8]=[(ord(c)-65)%32,(ord(c)-65)//32]
      a+=1
  return grid
def d_p(gr,COLORS,x,y):
  for i in gr:
    f(x+i[0],y+i[1],i[2],1,COLORS)
def cur(COLORS):
  f(pos[0]*27+5,pos[1]*27+3,27,2,COLORS)
  f(pos[0]*27+5,(1+pos[1])*27+1,27,2,COLORS)
  f(pos[0]*27+5,pos[1]*27+5,2,23,COLORS)
  f((1+pos[0])*27+3,pos[1]*27+5,2,23,COLORS)
def move(vx,vy):
  global pos, t
  if monotonic()-t>0.125:
    t=monotonic()
    cur(COLORS[((pos[0]+pos[1])%2)+2])
    pos[0]=(pos[0]+vx)%8
    pos[1]=(pos[1]+vy)%8
    cur(COLORS[4])
COLORS=(
(0,0,0),#black pieces
(220,170,80),#white pieces
(255,255,255),#white squares
(75,115,153),#black squares
(220,70,0),#cursor
(50,50,50),#background
(255,255,255),#text
(0,0,0),#white points text
(255,255,255))#black points text
key_pressing={"KEY_OK":0,"KEY_PLUS":0,"KEY_MINUS":0,"KEY_ZERO":0,"KEY_ONE":0,"KEY_TWO":0,"KEY_THREE":0,"KEY_FOUR":0,"KEY_FIVE":0,"KEY_SIX":0}
key_pressed={k:0 for k in key_pressing}
cr_ke={"KEY_ZERO": -1,"KEY_ONE": 0,"KEY_TWO": 1,"KEY_THREE": 2,"KEY_FOUR": 3,"KEY_FIVE": 4,"KEY_SIX": 5}
pieces_values=(1,3,3,5,9,0)
grid=c_g("DBCEFCBDAAAAAAAA8888aaaaaaaadbcefcbd")
sel=[0,(-1,-1),(0,0)]
pos=[0,0]
mov=1
str_txt=["black","white"]
f(0,0,320,222,COLORS[5])
for x in range(8):
  for y in range(8):
    f(x*27+5,y*27+3,27,27,COLORS[(y+x)%2+2])
for x in range(8):
  for y in range(8):
    if grid[x][y][0]>-1:
      d_p(gr_p[grid[x][y][0]],COLORS[grid[x][y][1]],x*27+7,y*27+5)
cur(COLORS[4])
d(str_txt[mov],248,3,COLORS[6],COLORS[5])
d("use",226,70,COLORS[6],COLORS[5])
d("ok",226,84,COLORS[6],COLORS[5])
d("switch",226,110,COLORS[6],COLORS[5])
d("plus",226,124,COLORS[6],COLORS[5])
d("unselect",226,150,COLORS[6],COLORS[5])
d("minus",226,164,COLORS[6],COLORS[5])
d("new piece",226,190,COLORS[6],COLORS[5])
d("0 to 6",226,206,COLORS[6],COLORS[5])
t=monotonic()
while 1:
  for k in key_pressing:
    key_pressed[k]=0
    if keydown(globals()[k]):
      if not key_pressing[k]:
        key_pressed[k]=1
      key_pressing[k]=1
    else:
      key_pressing[k]=0
  change=1
  if keydown(KEY_LEFT):
    move(-1,0)
  elif keydown(KEY_UP):
    move(0,-1)
  elif keydown(KEY_RIGHT):
    move(1,0)
  elif keydown(KEY_DOWN):
    move(0,1)
  if key_pressed["KEY_OK"]:
    if sel[0] and grid[pos[0]][pos[1]][1]!=sel[1][1]: 
      f((pos[0]*27)+7,(pos[1]*27)+5,23,23,COLORS[((pos[0]+pos[1])%2)+2])
      f((sel[2][0]*27)+7,(sel[2][1]*27)+5,23,23,COLORS[((sel[2][0]+sel[2][1])%2)+2])
      d_p(gr_p[sel[1][0]],COLORS[sel[1][1]],pos[0]*27+7,pos[1]*27+5)
      grid[sel[2][0]][sel[2][1]]=[-1,-1]
      grid[pos[0]][pos[1]]=sel[1]
      f(223,2,23,23,COLORS[5])      
      mov=not mov
      d(str_txt[mov],248,3,COLORS[6],COLORS[5])
      sel=[0,[-1,-1],[-1,-1]]
    elif grid[pos[0]][pos[1]][0]>-1 and sel[0]==0:
      if grid[pos[0]][pos[1]][1]==mov:
        sel=[1,tuple(grid[pos[0]][pos[1]]),tuple(pos)]
        d_p(gr_p[grid[pos[0]][pos[1]][0]],COLORS[grid[pos[0]][pos[1]][1]],223,2)
  elif key_pressed["KEY_MINUS"] or key_pressed["KEY_PLUS"]:
    sel=[0,[-1,-1],[-1,-1]]
    f(223,2,23,23,COLORS[5])
    if key_pressed["KEY_PLUS"]:
      mov=not mov
      d(str_txt[mov],248,3,COLORS[6],COLORS[5])
  elif 1 in [key_pressed[k] for k in cr_ke] :
    f(pos[0]*27+7,pos[1]*27+5,23,23,COLORS[((pos[0]+pos[1])%2)+2])
    for k in cr_ke:
      if key_pressed[k]:
        grid[pos[0]][pos[1]]=[cr_ke[k],mov]
    if grid[pos[0]][pos[1]][0]!=-1:
      d_p(gr_p[grid[pos[0]][pos[1]][0]],COLORS[mov],pos[0]*27+7,pos[1]*27+5)
    else:
      grid[pos[0]][pos[1]][1]=-1
  else:
    change=0
  if change:
    points=0
    for x in grid:
      for y in x:
        if y[1]==1:
          points+=pieces_values[y[0]]
        else:
          points-=pieces_values[y[0]]
    f(226,30,94,18,COLORS[5])
    if points>0:
      d(str(points),226,30,COLORS[7],COLORS[1])
    elif points<0:
      d(str(-1*points),226,30,COLORS[8],COLORS[0])
