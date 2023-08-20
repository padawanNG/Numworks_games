from math import *     # Importation du module math

print('====================================')
print(" Solveur d'équation du second degré ")  # Message de bienvenue !
print('====================================')
print("")


a = float(input("Valeur de a : "))
b = float(input("Valeur de b : "))           # On récupère les valeurs de a,b et c
c = float(input("Valeur de c : "))
x = int(input("Précision désirée en nbr de décimales : "))

print("")

if b > 0:
    bb=f"+{b}"
else:
    bb=f"{b}"
    
if c > 0:
    cc=f"+{c}"
else:
    cc=f"{c}"    

delta = b**2 - 4*a*c
print(f"{a}x²{bb}x{cc}")        # Calcul de delta, écriture de l'équation
print("")
print(f"Δ = {delta}")

if delta < 0:
    print("Δ < 0    Donc S = ∅ ")          # On détermine la ou les valeurs de x s'il y en a
elif delta == 0:
    print(f"Δ = 0   Donc x = {round((-b)/(2*a), x)}    Rappel : x = -b/2a")
else:
    print(f"Δ > 0   Donc x1 = {round((-b-sqrt(delta))/(2*a), x)}   x2 = {round((-b+sqrt(delta))/(2*a), x)}")

