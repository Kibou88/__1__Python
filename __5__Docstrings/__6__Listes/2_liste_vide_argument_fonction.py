# Liste vide comme argument d'une fonction
# - Utiliser une liste vide comme argument d'une fonction
#################################################
import random
def generateur_liste(liste=[]):
    liste.extend([random.randint(1, 100) for i in range(5)])
    return liste

for i in range(5):
    print(generateur_liste())
print()
#------------------------------------
def generateur_liste2(liste=None):
    if liste == None:
        liste = []
    liste.extend([random.randint(1, 100) for i in range(5)])
    return liste

for i in range(5):
    print(generateur_liste2())