# Coded by M-A G.  All rights reserved
import random

mots = ['table', 'chaise', 'caisse', 'arbre', 'pomme', 'orange', 'girafe', 'souris', 'banane', 'guitare', 'livre', 'ordinateur', 'ballon', 'voiture', 'camion', 'avion', 'escargot', 'hippopotame', 'crocodile', 'pingouin', 'cactus', 'guitare', 'brosse', 'bouteille', 'manege', 'manivelle', 'miroir', 'aspirateur', 'plante', 'flamant', 'lama', 'elephant', 'rhinoceros', 'grenouille', 'hibou', 'canard', 'papillon', 'tortue', 'licorne', 'grenade', 'couteau', 'fourchette', 'cuillere', 'baguette', 'volet', 'pompe', 'bicyclette', 'tricycle', 'moto', 'couronne', 'etoile', 'soleil', 'planete', 'comete', 'arcade', 'tunnel', 'aquarium', 'squelette', 'fantome', 'sirene', 'abeille', 'luciole', 'bonbon', 'citron', 'abricot', 'banjo', 'trompette', 'piano', 'violon', 'herisson', 'panda', 'koala', 'ecureuil', 'grenouille', 'souris', 'croissant', 'bagage', 'cartable', 'montagne', 'ocean', 'riviere', 'lac', 'nuage', 'orage', 'sourire', 'frisson', 'moustache', 'sabre', 'epee', 'chevalier', 'pirate', 'canon', 'fusil', 'grenade', 'pistolet']
mot=mots[random.randint(0,94)]
mot_en_cours=""
lettres=[]
essais=0
pas_fini=True
lettres_bannies="Lettres bannies : "
fails=6

for i in range(len(mot)):
    mot_en_cours+="_ "
    
print("-----------------------------------")
print(" Bienvenue au grand jeu du pendu ! ")
print("-----------------------------------")
    
    
while essais<6:
    print("")
    print("Mot en cours :",mot_en_cours)
    print(lettres_bannies)
    print("Fails restants :", fails)
    lettre=input("Quelle lettre ? ")
    if lettre in mot:
        print("La lettre \"",lettre,"\" est bien de le mot !")
        mot_en_cours=""
        lettres.append(lettre)
        for str in mot:
            if str in lettres:
                mot_en_cours+=str
                mot_en_cours+=" "
            else:
                mot_en_cours+="_ "
                
    else:
        print("Aïe ! La lettre \"",lettre,"\" n'est pas dans le mot !")
        essais+=1
        fails-=1
        lettres_bannies+=lettre
        lettres_bannies+=","
    
    for str in mot:
        if str in mot_en_cours:
            pas_fini=False
        else:
            pas_fini=True
            break
            
    if pas_fini==False:
        break
        

if pas_fini==True:
    print("")
    print("Aïe, tu as perdu !")
    print("Le mot à trouver était : \"",mot,"\"")
else:
    print("")
    print("Bravo, belle victoire !")
    print("Le mot à trouver était bel et bien \"",mot,"\"")

# Coded by M-A G.  All rights reserved    
