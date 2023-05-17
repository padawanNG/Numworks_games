from kandinsky import *
from random import randint
from ion import *

# Factors 1.4 NumWorks, 19.09.2022
# Par Ilyas R. & Vincent ROBERT
# https://nsi.xyz/factors <3

l_c,l_m,cursor,avg = 1,1,0,1.0
last_key,retry,in_level = None,False,False

rec = fill_rect
txt = draw_string

grid,pos = [1+i for i in range(16)],[]
sco = {0:0}
try:
    get_keys()
    os_c = (192,53,53)
except NameError:
    os_c = (255,183,52)

grey_c, dark_c, game_c, white_c = (196,196,196),(42,42,42),(148,113,222),(255,255,255)

# Le tuple `numbers` ainsi que la fonction `draw_number()` viennent d'Eric Schrafstetter
numbers = (31599,18724,29671,31207,18925,31183,31695,18727,31727,31215)
letters = (37583,188271,234063,74903,252783,186351,248271)

def fill(n,s):
    return "0"*(s-len(str(n)))+str(n)

def boot(key=420010100620):
    global l_c,l_m,avg,sco,last_key,retry,in_level
    if (key//1000)%sum(white_c)==key%1000 :
        l_m = int(str(key)[2:5])
        l_c = l_m
        avg = int(str(key)[5:7])+int(str(key)[7:10])/1000
        sco = {0:0,1:1}
        for level in range(1,l_m):
            sco[level] = 1
        for i in range(int((avg-1)*l_m)):
            sco[randint(max(l_m-10,1),max(l_m-1,1))] += 1
        last_key,retry,in_level = None,False,False
        factors()
    else:
        print("Invalid Key! Try again XD")

def generate_key():
    global l_m,avg
    if avg>99 or l_m>999:
        return "No backup possible"
    else:
        code_str = "42"+fill(l_m,3)+fill(int(avg),2)+fill(int((avg%1)*1000),2)
        hash_code = int(code_str)%sum(white_c)
        return code_str+fill(hash_code,3)

def save():
    print("[OK] Save progress feature ^^")
    print(generate_key())
    print("To load data, run")
    print("boot("+generate_key()+")")
    print("Press any key to continue")
    input()

def gui():
    for k in range(7):
        for i in range(19):
            if letters[k]>>i&1==1:
                rec(7+12*k+(i%3)*3,10+(i//3)*3,3,3,os_c)
    txt("Lvl",55,69,dark_c)
    txt("Avg",55,157,dark_c)
    rec(139,200,174,22,os_c)
    txt("Amusez-vous",22,202,grey_c)
    txt("",152,202,white_c,os_c)

def menu(in_menu=0):
    global l_c,avg,last_key,in_level
    rec(7,145,42,42,grey_c)
    avg_aff = str(round(avg)) if avg>=10 else str(round(avg,1))[:3]
    txt(str(avg_aff),13+5*(10<= avg<100),158,dark_c,grey_c)
    if in_menu==1:
        rec(7,57,42,42,game_c)
        refresh_scoreboard()
        txt("Play",8,37,dark_c)
        txt("Best",55,113,dark_c)
        rec(95,13,42,42*4+6,white_c)
        arrow(90,71,3,os_c)
        for i in range(4):
            for j in range(4):
                rec(139+44*j,13+44*i,42,42,grey_c)
        while not keydown(51) and not keydown(3):
            if keydown(1) and last_key!=1 and l_c!=l_m:
                l_c += 1
                last_key = 1
                refresh_scoreboard()
            if keydown(2) and last_key!=2 and l_c!=1:
                l_c -= 1
                last_key = 2
                refresh_scoreboard()
            if not (keydown(0) or keydown(1) or keydown(2) or keydown(3)):
                last_key = None
        in_level = False
        last_key = 3
    else:
        rec(7,57,42,42,grey_c)
        draw_number(l_c,7+44//2+center(l_c),13+58,dark_c)
        txt("Play",8,37,white_c)
        txt("Best",55,113,white_c)
        rec(0,101,60,42,white_c)
        if l_c==42:
            txt("^_^",55,113,game_c)

def refresh_scoreboard():
    rec(7,57,42,42,game_c)
    draw_number(l_c,7+44//2+center(l_c),13+58,dark_c)
    rec(0,101,42,42,white_c)
    if l_c!=l_m or (sco.get(l_c) is not None):
        txt(str(sco[l_c]),18+4*(sco[l_c]<10),113,dark_c)
        arrow(62,57,1,os_c if l_c!=l_m else white_c)
    else:
        arrow(62,57,1)
    if l_c != 1:
        arrow(62,92,2,os_c)
    else:
        arrow(62,92,2)

def center(nbr):
    if 0<nbr<10:
        ecart = -6
    elif 10<=nbr<100:
        ecart = -12
    elif 100<=nbr<1000:
        ecart = -18
    else:
        ecart = -26
    return ecart

def draw_number(n,x,y,c):
    if n>0:
        for k,j in enumerate(str(n)):
            for i in range(16):
                if numbers[int(j)]>>i&1==1:
                    rec(x+12*k+(i%3)*3,y+(i//3)*3,3,3,c)

def arrow(x,y,d,c=white_c):
    for i in range(6):
        if d==0:
            rec(x+i,y+6-i,1,2+2*i,c)
        if d==1:
            rec(x+6-i,y+i,2+2*i,1,c)
        if d==2:
            rec(x+i,y+i,12-2*i,1,c)
        if d==3:
            rec(x+i,y+i,1,12-2*i,c)

def generate_grid():
    for i in range(16):
        j = randint(1,15)
        grid[i],grid[j] = grid[j],grid[i]

def start_level(re=0,new=0):
    global cursor,pos,retry,l_c,l_m
    if new == 1:
        l_c += 1
        if l_c == l_m + 1:
            l_m += 1
    cursor = l_c
    pos = [0,1]
    arrow(62,57,1)
    arrow(62,92,2)
    arrow(90,71,3)
    arrow(0,71,0)
    rec(95,57,42,42,game_c)
    draw_number(l_c,d_p(pos[0])[0]+44//2+center(l_c),d_p(0,pos[1])[1]+44//2-8,dark_c)
    if not re:
        generate_grid()
    rec(d_p(5)[0],d_p(0,4)[1],0-176,0-176,white_c)
    k = 0
    for i in range(4):
        for j in range(4):
            rec(139+44*j,13+44*i,42,42,game_c)
            draw_number(grid[k],(139+44*j)+44//2+center(grid[k]),
                        (13+44*i)+44//2-8,white_c)
            k += 1
    retry = False

def move(key=3):
    global cursor,pos
    if 0<=pos[0]<=4 and 0<=pos[1]<=3:
        if key==3:
            rec(d_p(pos[0]-1)[0],d_p(pos[0],pos[1])[1],42,42,white_c)
            rec(d_p(pos[0])[0],13,42,42*4+3*2,white_c)
            number_interact=get_number(pos[0]-1,pos[1])
            if cursor%number_interact==0:
                cursor=cursor//number_interact
            else:
                cursor=cursor+number_interact
            rec(d_p(pos[0])[0],d_p(0,pos[1])[1],42,42,game_c)
            draw_number(cursor,d_p(pos[0])[0]+44//2+center(cursor),d_p(0,pos[1])[1]+44//2-8,dark_c)
        else:
            rec(d_p(pos[0])[0],d_p(pos[0],pos[1]+(-1 if key==2 else 1))[1],42,42,white_c)
            rec(d_p(pos[0])[0],d_p(0,pos[1])[1],42,42,game_c)
            draw_number(cursor,d_p(pos[0])[0]+44//2+center(cursor),d_p(0,pos[1])[1]+44//2-8,dark_c)

def get_number(x,y):
    return grid[y*4+x]

def d_p(p_x=0,p_y=0):
    return [95+44*p_x,13+44*p_y]

def level_transition(s):
    global l_c,l_m,avg,sco,pos
    k=0
    while d_p(pos[0])[0]+k != d_p(4)[0]:
        rec(d_p(pos[0])[0]+k,d_p(0,pos[1])[1],42,42,game_c)
        k+=1
    pos=[4,pos[1]]
    k=0
    while d_p(0,pos[1])[1]+k != d_p(0,3)[1]:
        rec(d_p(pos[0])[0],d_p(0,pos[1])[1]+k,42,42,game_c)
        k+=1
    pos=[4,3]
    k=0
    while k!=175:
        rec(d_p(pos[0]+1)[0]-2,d_p(0,pos[1]+1)[1]-2,0-k,0-k,game_c)
        k+=1
    txt("Perfect" if s==1 else "Well done" if s<=avg else "Can do better!!!",150 if s>avg else 185,50,white_c,game_c)
    draw_number(s,210,75,dark_c)
    txt("Retry",156,120,white_c,game_c)
    txt("Next",256,120,white_c,game_c)
    arrow(176,142,0,dark_c)
    arrow(266,143,3,dark_c)
    if l_c in sco:
        sco[l_c]=min(sco[l_c],s)
    else:
        sco[l_c]=s
    somme=0
    for value in sco.values():
        somme+=value
    avg=somme/(len(sco)-1*(len(sco)!=1))
    pos[0]=42

def factors():
    global cursor, pos, last_key, retry, in_level
    while not keydown(51):
        if in_level:
            if keydown(3) and last_key != 3:
                pos[0] += 1
                last_key = 3
                move(3)
            if keydown(0) and last_key != 0 and pos[0] > 0:
                retry = True
                last_key = 0
            elif keydown(0) and last_key != 0 and pos[0] == 0:
                pos[0] -= 1
            if keydown(1) and last_key != 1 and pos[1] > 0:
                pos[1] -= 1
                last_key = 1
                move(1)
            if keydown(2) and last_key != 2 and pos[1] < 3:
                pos[1] += 1
                last_key = 2
                move(2)
            if pos[0] == -1:
                menu(1)
            if retry:
                start_level(1)
                menu()
            if pos[0] == 4 or (cursor == 1 and not ((-1 <= pos[0] <= 0) or 42 <= pos[0] <= 43)):
                level_transition(cursor)
            if pos[0] == 43:
                start_level(0, 1)
                menu()
            if not (keydown(0) or keydown(1) or keydown(2) or keydown(3)):
                last_key = None
            if keydown(4):
                save()
                break
        else:
            gui()
            menu()
            start_level()
            in_level = True

factors()
# Your boot key:
