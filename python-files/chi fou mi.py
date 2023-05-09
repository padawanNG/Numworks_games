# Coded by M-A G.  All rights reserved

import random
from random import *

score=0
print ("---------------------------------------------------------------")
print ("Bienvenue au grand tournoi de CHI-FOU-MI (en trois manches) !!!")
print ("---------------------------------------------------------------")
for loop in range(3) :
 print ("Choisis ton coup en répondant par un chiffre : 1: PIERRE  2: FEUILLE  3: CISEAUX")
 j=int(input())
 if (j==1) :
  print ("PIERRE")
 if (j==2) :
  print ("FEUILLE")
 if (j==3) :
  print ("CISEAUX")
 print ("vs")
 n=randint(1, 3)
 if (n==1) :
  print ("PIERRE")
 if (n==2) :
  print ("FEUILLE")
 if (n==3) :
  print ("CISEAUX")
 if (j==n) :
  print ("Egalité, fin du match :)")
 if (j==1) and (n==2) :
  print ("J'ai joué FEUILLE et toi PIERRE, j'ai donc gagné ! Dommage :( ...")
 if (j==2) and (n==3) :
  print ("J'ai joué CISEAUX et toi FEUILLE, j'ai donc gagné ! Dommage :( ...")
 if (j==3) and (n==2) :
  print ("J'ai joué FEUILLE et toi CISEAUX, tu as donc gagné. Bravo !")
  score+=1
 if (j==1) and (n==3) :
  print ("J'ai joué CISEAUX et toi PIERRE, tu as don gagné. Bravo !")
  score+=1
 if (j==2) and (n==1) :
  print ("J'ai joué PIERRE et toi FEUILLE, tu as donc gagné. Bravo !")
  score+=1
 if (j==3) and (n==1) :
  print ("J'ai joué PIERRE et toi CISEAUX, j'ai donc gagné ! Dommage :( ...")
 print ("MANCHE SUIVANTE :")
print ("-------------------")
print ("Ton score est de...")
print (score)
print ("...points !")
print ("-------------------")
if (score==2) :
  print ("Bravo, TU AS GAGNE LE TOURNOI !!")
if (score==1) :
  print ("Dommage, tu n'as gagné qu'une fois sur trois. Tu as donc PERDU")
if (score==3) :
  print ("Bravo, tu as gagné le tournoi !!!")

  
  # Coded by M-A G.  All rights reserved
