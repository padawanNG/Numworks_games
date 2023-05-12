from random import choice
from kandinsky import fill_rect as rec, draw_string as txt
from ion import keydown as k
from time import sleep

# Reversi 1.2.1 NumWorks, 27.04.2023
# Par Thomas S. & Vincent ROBERT
# https://nsi.xyz/reversi

ai_lvl_list = ("Facile","Normal")
mode_de_jeu = ("J-2","IA")
directions = ([0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1])
col = ((100,203,111),(220,)*3,(60,)*3,(148,113,222),(242,0,0),(255,183,52),(255,)*3,(60,139,72),(90,)*3,(180,)*3,(160,)*3,(242,)*3)
len_x,len_y,c = 8,8,20
x_g = (320 - (1+len_x*(c+2))) // 2
y_g = (200 - (1+len_y*(c+2))) // 2

def grille(x, y, t_x, t_y, c, col):
  for w in range(t_x):
    for h in range(t_y):
      rec(1+x+w*(c+2), 1+y+h*(c+2), c, c, col)

def cercle(x,y,col,s=0):
  for d in range(6):
    rec(x-d+(d==0)+2*s, y+d+(d==5)+2*s, 6+2*d-2*(d==0)-4*s, 16-2*d-2*(d==5)-4*s, col)

def getCase(g_in, x, y, col_mode=False):
  if col_mode:
    if 0 <= g_in[y][x] <= 2:
      return col[g_in[y][x]]
    return None
  return -1 if x < 0 or x >= len_x or y < 0 or y >= len_y else g_in[y][x]

def setCase(g_in_in, x, y, value):
  g_in_in[y][x] = value

def wait(buttons=(0,1,2,3,4,5,52)):
  while True:
    for i in buttons:
      if k(i):
        while k(i): True
        return i

def deplacement(pos_old=[], for_error=False):
  global c
  if not(for_error):
    if pos_old != []:
      x, y = pos_old
      if getCase(g,x,y) in (1,2):
        rec(x_g+1+x*(c+2),y_g+1+y*(c+2),c,c,col[0])
        cercle(x_g+8+(c+2)*x,y_g+3+(c+2)*y,getCase(g,x,y,True))
      else:
        rec(x_g+1+x*(c+2),y_g+1+y*(c+2),c,c,getCase(g,x,y,True))
    x, y = pos
    rec(x_g+1+x*(c+2),y_g+1+y*(c+2),c,c,col[7])
    cercle(x_g+8+(c+2)*x,y_g+3+(c+2)*y,col[1] if player_turn == 1 else col[2],1)
    case = getCase(g,x,y)
    if case != 0:
      cercle(x_g+8+(c+2)*x,y_g+3+(c+2)*y,getCase(g,x,y,True))
  else:
    rec(x_g + 1 + pos[0]*(c+2),y_g + 1 + pos[1]*(c+2), c, c, col[4])
    sleep(0.1542)
  affichage()

def update():
  global c
  for y in range(len_y):
    for x in range(len_x):
      if getCase(g,x,y) in (1,2):
        rec(x_g+1+x*(c+2), y_g+1+y*(c+2), c, c, col[0])
        cercle(x_g+8+(c+2)*x, y_g+3+(c+2)*y, getCase(g, x, y, True))
      else:
        rec(x_g+1+x*(c+2), y_g+1+y*(c+2), c, c, getCase(g, x, y, True))
  deplacement()

def affichage():
  if param == 1:
    txt("<", 283-len(mode_de_jeu[ai_enable_indice])*5-15, y_g+2, col[10])
    txt(">",283+len(mode_de_jeu[ai_enable_indice])*5+5, y_g+2, col[10])
  elif param == 2:
    txt("<", 283-15, y_g+(c+2)*7+17, col[10])
    txt(">",283+5,y_g+(c+2)*7+17,col[10])
  txt("J-1",20,y_g+2,col[8])
  cercle(32,y_g+c+2+3,col[2])
  txt("Score",10,y_g+(c+2)*3+2,col[8])
  rec(25,y_g+(c+2)*4+2,22,18,col[6])
  txt(str(sc_noir),35-len(str(sc_noir))*5,y_g+(c+2)*4+2,col[9])
  if not(no_round in (0,2)):
    rec(9,y_g+(c+2)*6+1,52,(c+2)*2, col[3])
    txt("Tour",15,y_g+(c+2)*6+2, col[11], col[3])
    txt("passé",10,y_g+(c+2)*7+2, col[11], col[3])
    sleep(0.242)
  else:
    rec(9,y_g+(c+2)*6+1, 52, (c+2)*2, col[6])
  txt(mode_de_jeu[ai_enable_indice],283-len(mode_de_jeu[ai_enable_indice])*5,y_g+2,col[8])
  cercle(280,y_g+c+2+3,col[1])
  txt("Score",258,y_g+(c+2)*3+2,col[8])
  rec(273,y_g+(c+2)*4+2,22,18,col[6])
  txt(str(sc_blanc),283-len(str(sc_blanc))*5,y_g+(c+2)*4+2,col[9])
  if sets["ai_enable"]:
    txt("Niveau",253,y_g+(c+2)*6+2,col[8])
    txt(ai_lvl_list[ai_lvl_indice],283-len(ai_lvl_list[ai_lvl_indice])*5,y_g+(c+2)*7+2,col[9])
  if sc_noir == 42:
    txt("<3",25,y_g+(c+2)*5+2,(255,0,0))
  else:
    rec(25,y_g+(c+2)*5+2,20,18,col[6])
  if sc_blanc == 42:
    txt("<3",273,y_g+(c+2)*5+2,(255,0,0))
  else:
    rec(273,y_g+(c+2)*5+2,20,18,col[6])

def do_pion(mode, pion_x, pion_y, directions_in, ai_ask=False):
  if getCase(g,pion_x, pion_y) != 0:
    return False
  result = []
  if ai_ask:
    dist_totale = []
  global sc_noir,sc_blanc
  pion_adverse = 1 if player_turn == 2 else 2
  for d in directions_in:
    x,y,dir_x,dir_y = pion_x,pion_y,d[0],d[1]
    current = getCase(g, x + dir_x, y + dir_y)
    dist_parcourue = 1
    while pion_adverse == current:
      x,y = x+dir_x,y+dir_y
      if mode == 1:
        sc_blanc += 1-2*(player_turn!=1)
        sc_noir += 1-2*(player_turn!=2)
        setCase(g, x, y, player_turn)
      current = getCase(g, x + dir_x, y + dir_y)
      dist_parcourue += 1
    if mode == 0 and dist_parcourue > 1 and current == player_turn:
      if not(ai_ask):
        result.append(d)
      else:
        dist_totale.append(dist_parcourue)
        result.append(d)
    else:
      continue
  if mode == 1:
    if player_turn == 1:
      sc_blanc += 1
    else:
      sc_noir += 1
    setCase(g,pion_x,pion_y,player_turn)
  else:
    if ai_ask:
      result.append(sum(dist_totale))
    return result

def has_legal_hit():
  legal_hits = []
  for y in range(len_y):
    for x in range(len_x):
      if do_pion(0,x,y,directions):
        legal_hits.append([x,y])
  return legal_hits

def ai(lvl):
  if lvl == 0:
    return choice(has_legal_hit())
  elif lvl == 1:
    legal_hits = has_legal_hit()
    temp = []
    plus_grand = [[],0]
    for i in range(len(legal_hits)):
      legal_hits[i] = [legal_hits[i],do_pion(0,legal_hits[i][0],legal_hits[i][1],directions,True)]
    for i in legal_hits:
      if i[1][-1] > plus_grand[1]:
        plus_grand = [[i[0]],i[1][-1]]
      elif i[1][-1] == plus_grand[1]:
        plus_grand[0].append(i[0])
    return choice(plus_grand[0])

def action(position):
  global player_turn
  result = do_pion(0,position[0],position[1],directions)
  if result != [] and result != False:
    do_pion(1,position[0],position[1],result)
    player_turn = 1 if player_turn == 2 else 2
    update()
  else:
    deplacement(for_error=True)

def gameover():
  rec(0,200,320,22,col[5])
  txt("Terminé ! Relancer avec OK",30,202,col[11],col[5])
  while 1:
    key_pressed = wait()
    if key_pressed in (4,52):
      break
  init()

def init():
  global sets,g,player_turn,sc_noir,sc_blanc,no_round,pos,ai_enable_indice,ai_lvl_indice,param
  sets = {"player_choice": 2,"ai_enable": False, "ai_lvl": 0}
  g = [[0 for i in range(len_x)] for i in range(len_y)]
  g[3][3],g[3][4],g[4][3],g[4][4] = 1,2,2,1
  player_turn,sc_noir,sc_blanc,no_round = 2,0,0,0
  pos = [2,3]
  rec(0,0,320,200,col[6])
  rec(0,200,320,22,col[3])
  txt("Code by programmes-numworks.fr",45,202,col[11],col[3])
  grille(x_g,y_g,len_x,len_y,c,col[0])
  param = 1
  ai_enable_indice = 1
  ai_lvl_indice = 0
  affichage()
  while 1:
    key_pressed = None
    key_pressed = wait()
    if key_pressed == 0:
      if param == 1:
        ai_enable_indice = (ai_enable_indice-1) % 2
      elif param == 2:
        ai_lvl_indice = (ai_lvl_indice-1) % 2
    elif key_pressed == 3:
      if param == 1:
        ai_enable_indice = (ai_enable_indice+1) % 2
      elif param == 2:
        ai_lvl_indice = (ai_lvl_indice+1) % 2
    if key_pressed in (4,52):
      if param == 1:
        if ai_enable_indice == 1:
          sets["ai_enable"] = True
          param += 1
        else:
          sets["ai_enable"] = False
          param = 0
          rec(248,y_g+2,71,18,col[6])
          break
      else:
        if sets["ai_enable"]:
          sets["ai_lvl"] = 0 if ai_lvl_indice == 0 else 1
        param = 0
        rec(248,y_g+(c+2)*7+17,71,18,col[6])
        break
    if key_pressed == 5 and param == 2:
      param -= 1
      sets["ai_enable"] = False
      rec(248,y_g+(c+2)*6+2,71,55,col[6])
    if key_pressed != None:
      rec(248,y_g+2,71,18,col[6])
      rec(248,y_g+(c+2)*7+2,71,18,col[6])
      affichage()
  play()

def play():
  global player_turn,sc_noir,sc_blanc,no_round
  sc_noir,sc_blanc = 2,2
  update()
  while 1:
    key_pressed = None
    pos_old = list(pos)
    if has_legal_hit() == []:
      player_turn = 1 if player_turn == 2 else 2
      no_round += 1
      if no_round == 2:
        affichage()
        break
      affichage()
      continue
    else:
      no_round = 0
    if sets["ai_enable"] and player_turn != sets["player_choice"]:
      sleep(0.242)
      pos_ai = ai(sets["ai_lvl"])
      action(pos_ai)
      continue
    key_pressed = wait()
    if key_pressed == 1:
      pos[1] = (pos[1]-1) % 8
    elif key_pressed == 2:
      pos[1] = (pos[1]+1) % 8
    elif key_pressed == 3:
      pos[0] = (pos[0]+1) % 8
    elif key_pressed == 0:
      pos[0] = (pos[0]-1) % 8
    elif key_pressed in (4,52):
      if sets["ai_enable"] and player_turn == sets["player_choice"]:
        action(pos)
      elif not(sets["ai_enable"]):
        action(pos)
    if key_pressed != None:
      deplacement(pos_old)
  gameover()
init()
