# Coded by M-A G.  All rights reserved

# Importation des modules
from kandinsky import *
from ion import *
from time import *

# Creation la grille (6*7)
def mise_en_place():
  fill_rect(0,0,320,250,"white")
  for i in range(7):
    fill_rect(40,28*i+42,241,3,"black")    
  for i in range(8):
    fill_rect(34*i+40,45,3,165,"black")

mise_en_place()

# Fonction trace de cercle
def circle(x,y,couleur):
  fill_rect(x-11,y-3,23,7,couleur)
  fill_rect(x-10,y-5,21,11,couleur)
  fill_rect(x-9,y-7,19,15,couleur)
  fill_rect(x-8,y-8,17,17,couleur)
  fill_rect(x-7,y-9,15,19,couleur)
  fill_rect(x-5,y-10,11,21,couleur)
  fill_rect(x-3,y-11,7,23,couleur)
    

# Fonction de vérification de victoire
  

# Fonction du jeton qui tombe
def fall(selection,couleur,ligne):
  if remplissage[selection-1]!=0:
    circle(34*selection+24,23,"white")
    circle(34*selection+24,28*ligne+42+15,couleur)
    sleep(0.2)
    for i in range(remplissage[selection-1]-1):
      circle(34*selection+24,28*ligne+42+15,"white")  
      ligne+=1
      circle(34*selection+24,28*ligne+42+15,couleur)  
      sleep(0.2)    
      
# Variables utiles
selection=4
couleur="red"
jeu_fini = False
ligne=0
remplissage=[6,6,6,6,6,6,6]
compteur=0

# Premier jeton !
circle(160,23,couleur)

# Boucle principale
while jeu_fini==False:  
  if keydown(KEY_LEFT):
    sleep(0.25)
    circle(34*selection+24,23,"white")
    if selection!=1:
      selection-=1
    else:
      selection=7
    circle(34*selection+24,23,couleur)  
  if keydown(KEY_RIGHT):
    sleep(0.25)
    circle(34*selection+24,23,"white")
    if selection!=7:
      selection+=1
    else:
      selection=1
    circle(34*selection+24,23,couleur)
    
  if keydown(KEY_OK) or keydown(KEY_EXE) or keydown(KEY_DOWN):
    fall(selection,couleur,ligne)
    if remplissage[selection-1]!=0:
      if couleur=="red":
        couleur="yellow"
      else:
        couleur="red"  
      circle(160,23,couleur)
      remplissage[selection-1]-=1      
      selection=4
    sleep(0.15)  
        
  if keydown(KEY_ZERO):
    mise_en_place()   
    couleur="red"
    circle(160,23,couleur)
    for i in range(7):
      remplissage[i]=6
    selection=4  
    sleep(0.2)
  
  if remplissage[0]+remplissage[1]+remplissage[2]+remplissage[3]+remplissage[4]+remplissage[5]+remplissage[6]==0 and jeu_fini==False:
    circle(34*selection+24,23,"white")
    draw_string("Match nul",120,13)
    break

# Coded by M-A G.  All rights reserved    
