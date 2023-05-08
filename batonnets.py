# Coded by M-A G.  All rights reserved

import random
from time import *

j=int(input("Jouer à 1 ou 2 : "))
u=random.randint(20,40)
sleep(0.15)
print("")
print("---------------------------------------")
print("Bienvenue dans le jeu des batonnets !!!")
print("---------------------------------------")
print("")
sleep(0.15)
print("Nous allons jouer avec",u,"batonnets")
print("")
sleep(0.15)
if j==1:
    m=random.randint(1,2)
    if m==1:
        print("Le bot va commencer !")
    else:
        print("C'est toi qui va commencer !")

sleep(0.2)

while u!=1:
  if j==1:
    if m==2:
      f=""
      for i in range(u):
        f+="|"
      print("Les batons:",f)
      print("Il y en a ", u)
      l=int(input("Joueur 1, prends-tu 1, 2 ou 3 batons :"))
      if u-l<1:
        print("Cela ne marche pas, passe ton tour...")
      if u-l>0:
        u-=l
      if u==1:
        print("")  
        print("------------------------")
        print("Victoire du joueur 1 !!!")
        print("------------------------")
        break
      if u!=1:
        f=""
      for i in range(u):
        f+="|"
      a=random.randint(1,3)
      print("")
      print("Les batons:",f)
      print("Il y en a ",u)
      if u-a<1:
        print("Cela ne marche pas, le bot passe ton tour...")
      if u-a>0:
        u-=a
      print("Le bot a pris",a,"batons...")
      print("")
      if u==1:
        print("")  
        print("-------------------")
        print("Victoire du bot !!!")
        print("-------------------")
        break

    if m==1:
      f=""
      for i in range(u):
        f+="|"
      print("Les batons:",f)
      print("Il y en a ", u)
      a=random.randint(1,3)
      if u-a<1:
        print("Cela ne marche pas, le bot passe ton tour...")
      if u-a>0:
        u-=a
      if u==1:
        print("")
        print("-------------------")
        print("Victoire du bot !!!")
        print("-------------------")
        break
      if u!=1:
        f=""
      for i in range(u):
        f+="|"
      print("Les batons:",f) 
      print("Il y en a ", u)
      l=int(input("Joueur 1, prends-tu 1, 2 ou 3 batons :"))
      if u-l<1:
        print("Cela ne marche pas, passe ton tour...")
      if u-l>0:
        u-=l
      if u==1:
          print("")
        print("------------------------")
        print("Victoire du joueur 1 !!!")
        print("------------------------")
        
################################################################################################
  if j==2:
    f=""
    for i in range(u):
      f+="|"
    print("")  
    print("Les batons:",f)
    print("Il y en a ", u)
    l=int(input("Joueur 1, prends-tu 1, 2 ou 3 batons : "))
    if u-l<1:
      print("Cela ne marche pas, passe ton tour...")
    if u-l>0:
      u-=l
    if u==1:
      print("")  
      print("------------------------")
      print("Victoire du joueur 1 !!!")
      print("------------------------")
      break
    f=""
    for i in range(u):
      f+="|"
    if u!=1:
      print("")
      print("Les batons:",f)
      print("Il y en a ", u)
      w=int(input("Joueur 2, prends-tu 1, 2 ou 3 batons : "))
      if u-w<1:
        print("Cela ne fonctionne pas, passe ton tour...")
      if u-w>0:
        u-=w
    if u==1:
      print("")  
      print("------------------------")
      print("Victoire du joueur 2 !!!")
      print("------------------------")
      print("")
      break
# Coded by M-A G.  All rights reserved
