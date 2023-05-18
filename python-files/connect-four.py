# Credits : Robin C.
# https://nsi.xyz/numapps/puissance-4-en-python-numworks/

from kandinsky import fill_rect as rect, draw_string as txt
from time import sleep
from ion import keydown

# Puissance 4 1.01 NumWorks, 23.04.2023
# Par Robin C. & Vincent ROBERT
# https://nsi.xyz/puissance4

# 1 = rouge // 2 = jaune

# Variables globales
player = 1
grille = [[0 for i in range(7)] for i in range(6)]

rouge = (182, 2, 5)
jaune = (255, 181, 49)
gris = (191, 189, 193)

pos = 3

points_rouge = 0
points_jaune = 0

def verifie(): #Vérifie si il y a un gagnant
   for i in range(6): #lignes
      for j in range(4):
         if grille[i][j] == player and grille[i][j+1] == player and grille[i][j+2] == player and grille[i][j+3] == player:
            gagnant(player)
   for i in range(3): #colonnes
      for j in range(7):
         if grille[i][j] == player and grille[i+1][j] == player and grille[i+2][j] == player and grille[i+3][j] == player:
            gagnant(player)
   for i in range(3): #diagonales
      for j in range(4):
         if grille[i][j] == player and grille[i+1][j+1] == player and grille[i+2][j+2] == player and grille[i+3][j+3] == player:
            gagnant(player)
   for i in range(3, 6):
      for j in range(4):
         if grille[i][j] == player and grille[i-1][j+1] == player and grille[i-2][j+2] == player and grille[i-3][j+3] == player:
            gagnant(player)

def gagnant(winner): #Met fin à une partie gagnant ou pas
   global points_jaune, points_rouge, player, nb_partie, grille, partie
   affichage_grille()
   if winner == 1 :
      points_rouge += 1
      player = 2
      txt("Rouge a gagné !", 88, 20)
   elif winner == 2 :
      points_jaune += 1
      player = 1
      txt("Jaune a gagné !", 88,20)
   else :
      txt("C'est une égalité", 76, 20)
   wait()
   actu_src()
   grille = [[0 for i in range(7)] for i in range(6)]
   affichage_grille()

def selection():
   global pos
   affichage_grille()
   affichage_preview(pos)
   add = 1
   while True :
      affichage_preview(pos)
      while colonne_pleine(pos):
         pos = (pos+add)%7
         affichage_preview(pos)
      key_pressed = wait()
      if key_pressed == 0:
         add = -1
      if key_pressed == 3:
         add = +1
      if key_pressed==0 or key_pressed==3:
         pos = (pos+add)%7
         affichage_preview(pos)
      if key_pressed == 4 or key_pressed == 52 :
         rect(75, 17, 170, 20, (255,255,255))
         jouer(pos)

def jouer(colonne): # Ajoute un jeton dans la colonne donnée
   global player
   if player == 1 :
      animation(colonne)
      grille[gravite(colonne)][colonne] = 1
      verifie()
      player = 2
   elif player == 2 :
      animation(colonne)
      grille[gravite(colonne)][colonne] = 2
      verifie()
      player = 1
   grille_pleine()

def animation(colonne): #Animation de la chute du jeton
   if player == 1 :
      color = rouge
   else :
      color = jaune
   for i in range(0, gravite(colonne)+1):
         ligne = (i-1)*(i!=0)
         rect(75+(25*colonne),42+(ligne*25),20,20,gris)
         sleep(0.05)
         draw_cercle(75 + (25*colonne) + 7, 42 + (i*25) + 2, color)
         sleep(0.05)

def draw_cercle(x,y,color): #Fait des cercles (Par VR)
   for d in range(6):
      rect(x-d+(d==0),y+d+(d==5),6+2*d-2*(d==0),16-2*d-2*(d==5), color)

def colonne_pleine(colonne):
   if (grille[0][colonne] == 1) or (grille[0][colonne] == 2):
      return True
   return False

def grille_pleine(): #Vérifie si il y a une égalité soit si la grille est pleine
   colonne_pleines = 0
   for i in range(7):
      if colonne_pleine(i):
         colonne_pleines += 1
   if colonne_pleines == 7:
      gagnant(0)

def gravite(colonne): #Détermine la ligne où le jeton peut se placer
   ligne = 5
   while grille[ligne][colonne] != 0:
      if ligne == 0 :
         return ligne
      ligne -= 1
   return ligne

def affichage_grille():
   rect(75, 42, 175, 150, (255,255,255))
   pos_x, pos_y_base, marge = 50, 42, 25
   for i in range(7):
      pos_x += marge
      pos_y = pos_y_base
      for y in range(6):
         cote = 20
         if grille[y][i] == 1:
            color = rouge
         elif grille[y][i] == 2:
            color = jaune
         else :
            color = gris
         if grille[y][i] == 1 or grille[y][i] == 2:
            rect(pos_x, pos_y, cote, cote, gris)
            draw_cercle(pos_x + 7, pos_y + 2,color)
         else:
            rect(pos_x, pos_y, cote, cote, gris)
         pos_y += marge

def affichage_preview(col_preview):
   rect(75, 17, 170, 20, (255,255,255))
   if player == 1 :
      color = rouge
   else :
      color = jaune
   draw_cercle(75 + (col_preview * 25) + 7, 17+2, color)

def wait(buttons=(0,1,2,3,4,52)): #Retourne la touche appuyée
   while True:
      for i in buttons:
         if keydown(i):
            while keydown(i): True
            return i

#Score par Thomas S. mais code par Robin C.
def affichage_src():
   txt("J-1", 22, 42)
   draw_cercle(35,70,rouge)
   txt("Score", 12, 117)
   if points_rouge < 10 :
      largeur = 32
   else :
      largeur = 27
   txt(str(points_rouge),32,142)
   txt("J-2", 267, 42)
   draw_cercle(280,70,jaune)
   txt("Score", 257, 117)
   if points_jaune < 10 :
      largeur = 277
   else :
      largeur = 272
   txt(str(points_jaune),277,142)

def actu_src(): #Actualise le score
   txt(str(points_rouge),37-5*len(str(points_rouge)),142)
   txt(str(points_jaune),282-5*len(str(points_jaune)),142)

#Lien article
rect(0,200,320,22,(148,113,222))
txt("Code by programmes-numworks.fr",11,202,(242,)*3,(148,113,222))

affichage_src()
selection()

# Credits : Robin C.
# https://nsi.xyz/numapps/puissance-4-en-python-numworks/
