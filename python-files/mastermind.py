from kandinsky import draw_string as txt, fill_rect as rec
from ion import keydown
from random import choice
from math import factorial as fact

# Mastermind 1.0 NumWorks, 11.02.2023
# Par Ilyas R. & Vincent ROBERT
# https://nsi.xyz/mastermind <3

dark_c=(42,)*3
light_c=(142,)*3
bright_c=(242,)*3
game_c=(148,113,222)
void_c=(255,)*3

colors=((255,89,94),(255,202,58),(81,176,201),(138,201,38),(255,146,76),(142,)*3,(71,103,212),(82,166,117))
cursor=color=lvl=0

scoreboard=[["Score",0],["Max",0],["Legit",0],[None]]

game_config=(["Colors",8],["Code",4],["Dupli", 1],["Help",0])
config_limits=((5,8),(3,6),[0,1],(0,1))
game=combin=[]
state="IN_MENU"
ks=0


def reset():
    global cursor,color,lvl,scoreboard,game,combin
    rec(0,0,320,222,void_c)
    cursor=color=lvl=0
    scoreboard=[["Score",0],["Max",0],["Legit",0],[None]]
    game=combin=[]


def gui(e=0):
    rec(0,200,320,22,game_c)
    txt("",33,202,bright_c,game_c)
    for i in range(len(game_config)):
        txt(game_config[i][0],40 -5*len(game_config[i][0]),200//(len(game_config)+1)*(i + 1)-18,light_c)
        rec((81-18)//2,200//(len(game_config)+1)*(i+1),18,18,light_c)
        txt(str(game_config[i][1]),(81-18)//2+4,200//(len(game_config)+1)*(i+1),bright_c,light_c)
    for i in range(4):
        arrow(268+3*(i>0),160,i,light_c)
    txt("OK",269,160,dark_c)
    if not e:
        plateau(game_config[1][1])
        config_displayer(0,1)
        calc_max()
    arrows_displayer(0,1*(e!=0))


def plateau(code):
    rec(101,1,118,198,void_c)
    for i in range(10):
        for j in range(code):
            set_cell((j,i),bright_c)


def config_displayer(conf,stt):
    c=game_c if stt else light_c
    txt(game_config[conf][0],40-5*len(game_config[conf][0]),200//(len(game_config)+1)*(conf+1)-18,c)
    rec((81-18)//2,200//(len(game_config)+1)*(conf+1),18,18,c)
    txt(str(game_config[conf][1]),(81-18)//2+4,200//(len(game_config)+1)*(conf+1),bright_c,c)


def config_updater(conf,incr,f=0):
    global game_config
    c=light_c if f else game_c
    game_config[conf][1]+=incr
    txt(str(game_config[conf][1]),(81-18)//2+4,200//(len(game_config)+1)*(conf+1),bright_c,c)
    arrows_displayer(conf)
    if conf<=3:
        if conf==1:
            plateau(game_config[conf][1])
        calc_max()
    else:
        scoreboard_displayer()


def arrows_displayer(conf,leave=0):
    if leave:
        for i in range(len(game_config)):
            for j in range(2):
                rec((81-18)//2+(25 if j else -17),200//(len(game_config)+1)*(i+1)+3,10,10,void_c)
    else:
        if game_config[conf][1]>config_limits[conf][0]:
            txt("<",(81-18)//2-17,200//(len(game_config)+1)*(conf+1),game_c)
        else:
            txt("<",(81-18)//2-17,200//(len(game_config)+1)*(conf+1),void_c)
        if game_config[conf][1]<config_limits[conf][1]:
            txt(">",(81-18)//2+25,200//(len(game_config)+1)*(conf+1),game_c)
        else:
            txt(">",(81-18)//2+25,200//(len(game_config)+1)*(conf+1),void_c)


def arrow(x,y,d=0,c=game_c):
    for i in range(6):
        rec(x+(23+i)*(d==3)-(5+i)*(d==0)+(3+i)*(d%3!=0),y+(3+i)*(d%3==0)-(7+i)*(d==1)+(22+i)*(d==2),1,2,c)
        rec(x+(23+i)*(d==3)-(5+i)*(d==0)+(13-i)*(d%3!=0),y+(13-i)*(d%3==0)-(7+i)*(d==1)+(22+i)*(d==2),1,2,c)


def config_manager(conf,i):
    config_displayer(conf,0)
    arrows_displayer(conf,1)
    conf+=i
    config_displayer(conf,1)
    arrows_displayer(conf)


def config_dupli_manager(conf):
    if game_config[1][1]>game_config[0][1]:
        game_config[2][1]=1
        config_limits[2][0]=1
        config_updater(2,0,1*(conf!=2))
    else:
        config_limits[2][0]=0


def menu():
    global game,ks
    config=0
    last_key=None
    while not (keydown(4) or keydown(52)) or not ks:
        if keydown(1) and config>0 and last_key!=1:
            config_manager(config,-1)
            config-=1
            last_key=1
        if keydown(2) and config<len(game_config)-1 and last_key!=2:
            config_manager(config,1)
            config+=1
            last_key=2
        if keydown(0) and game_config[config][1]>config_limits[config][0] and last_key!=0:
            config_updater(config,-1)
            last_key = 0
        if keydown(3) and game_config[config][1]<config_limits[config][1] and last_key!=3:
            config_updater(config,1)
            last_key=3
        config_dupli_manager(config)
        if not (keydown(0) or keydown(1) or keydown(2) or keydown(3) or keydown(4) or keydown(52)):
            last_key,ks = None,1
    gui(1)
    game=[["" for _ in range(game_config[1][1])] for _ in range(10)]
    indicators_manager(1)


def d_p(p_x=0,p_y=0):
    return (320-(game_config[1][1]*20-2))//2+20*p_x,181-20*p_y


def set_cell(pos,c):
    rec(d_p(pos[0])[0],d_p(p_y=pos[1])[1],18,18,c)


def indicators_manager(static=0,dyn_del=0,dyn_place=0):
    if static:
        arrow(d_p(-1)[0]+16,d_p(p_y=lvl)[1],0)
        arrow(d_p(game_config[1][1])[0]-16,d_p(p_y=lvl)[1],3)
        arrow(d_p(cursor)[0]+1,d_p(p_y=lvl)[1]+17,1,bright_c)
        arrow(d_p(cursor)[0]+1,d_p(p_y=lvl+1)[1]+17,1)
    if dyn_del:
        for i in range(game_config[1][1]):
            arrow(d_p(i)[0]+1,d_p(p_y=lvl+1)[1]+17,1,bright_c)
    if dyn_place:
        arrow(d_p(cursor)[0]+1,d_p(p_y=lvl+1)[1]+17,1)


def generate_combination():
    suit=[]
    while not suit or (len(set(suit))!=len(suit) and game_config[2][1]!=1):
        suit=[choice([i for i in range(game_config[0][1])]) for _ in range(game_config[1][1])]
    return suit


def check_line(line,secret):
    good=sum([line[i]==secret[i] for i in range(len(line))])
    bad=sum([line[i] in secret for i in range(len(line))])-good
    return bad,good


def check_manager():
    bad,good=check_line(game[lvl],combin)
    txt(str(bad),d_p(-1)[0]+ 4,d_p(p_y=lvl)[1],"red",void_c)
    txt(str(good),d_p(game_config[1][1])[0]+4,d_p(p_y=lvl)[1],"green",void_c)
    win_manager(bad,good)


def scoreboard_manager(init=0):
    if init:
        scoreboard[0][1]=100000
        calc_max()
        scoreboard_displayer()
    else:
        if game_config[3][1]:
            legit_eval()


def calc_max():
    if game_config[2][1]:
        combi=game_config[0][1]**game_config[1][1]
    else:
        combi=fact(game_config[0][1])//fact(game_config[0][1]-game_config[1][1])
    scoreboard[1][1]=combi
    scoreboard_displayer()


def scoreboard_displayer():
    rec(255,105,49,30,void_c)
    for i in range(2+1*(game_config[3][1])):
        txt(scoreboard[i][0],280-5*len(scoreboard[i][0]),200//(len(scoreboard)+1)*(i+1)-18,dark_c)
        rec(250,200//(len(scoreboard)+1)*(i+1),60,18,void_c)
        txt(str(scoreboard[i][1]),280-5*len(str(scoreboard[i][1])),200//(len(scoreboard)+1)*(i+1),light_c)


def win_manager(b,g):
    global lvl,state,ks
    scoreboard[0][1]=int(scoreboard[0][1]*(0.80 + 0.2*g/game_config[1][1]+0.1*b/game_config[1][1]))
    if g==game_config[1][1]:
        rec(244,148,70,42,game_c)
        txt("WIN",264,160,bright_c,game_c)
        state,ks ="END",1
    elif lvl==9:
        rec(244,148,70,42,game_c)
        txt("LOOSE",254,160,bright_c,game_c)
        state,ks ="END",1
    scoreboard_displayer()


def legit_eval():
    global lvl
    ok=0
    for i in range(1000):
        if not i%100:
            rec(255+5*i//100,120,5,18,game_c)
        test=generate_combination()
        for j in range(lvl + 1):
            if check_line(game[j],combin)!=check_line(game[j],test):
                break
            if j==lvl:
                ok+=1
    result=max(0.1,round(ok/10,1))
    scoreboard[2][1]=str(result)+"%"


def start():
    global cursor, color, lvl, game, combin, state
    state = "IN_GAME"
    last_key = None
    gui()
    scoreboard_displayer()
    menu()
    combin = generate_combination()
    scoreboard_manager(1)
    while state != "END":
        if keydown(0) and last_key != 0:
            indicators_manager(dyn_del=1)
            cursor -= 1
            cursor = cursor % game_config[1][1]
            indicators_manager(dyn_place=1)
            last_key = 0
        if keydown(3) and last_key != 3:
            indicators_manager(dyn_del=1)
            cursor += 1
            cursor = cursor % game_config[1][1]
            indicators_manager(dyn_place=1)
            last_key = 3
        if keydown(1) and last_key != 1:
            color = (game[lvl - 1][cursor] - 1) % game_config[0][1] if game[lvl][cursor] == "" and lvl != 0 else color
            color += 1
            game[lvl][cursor] = color % game_config[0][1]
            set_cell((cursor, lvl), colors[color % game_config[0][1]])
            last_key = 1
        if keydown(2) and last_key != 2:
            color = (game[lvl - 1][cursor] + 1) % game_config[0][1] if game[lvl][cursor] == "" and lvl != 0 else color
            color -= 1
            game[lvl][cursor] = color % game_config[0][1]
            set_cell((cursor, lvl), colors[color % game_config[0][1]])
            last_key = 2
        if (keydown(4) or keydown(52)) and "" not in game[lvl] and (last_key != 4 or last_key != 52):
            scoreboard_manager()
            check_manager()
            lvl += 1
            indicators_manager(1)
            last_key = 4
        if not (keydown(0) or keydown(1) or keydown(2) or keydown(3) or keydown(4) or keydown(52)):
            last_key = None


def mastermind():
    global ks
    while not keydown(51):
        if state == "IN_MENU":
            start()
        if state == "END" and (keydown(4) or keydown(52)) and not ks:
            reset()
            start()
        if not (keydown(4) or keydown(52)):
            ks = 0


mastermind()
