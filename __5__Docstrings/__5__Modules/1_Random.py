# Module Random
# - Apprendre le fonctionnement du module random
################################################

import random

# 0 et 10 définissent la plage de fonctionnement du module random
aleatoire1 = random.randint(0,10) # Retourne un nombre entier aléatoire
aleatoire2 = random.uniform(0,10) # Retourne un nombre décimal aléatoire

# randrange définit une plage de 0 (défaut) à 999 (non inclus)
aleatoire3 = random.randrange(999) # Retourne un nombre entier aléatoire
aleatoire4 = random.randrange(0,101,10) # Retourne un nombre aléatoire compris entre 0 et 100 (inclus)
# par pas de 10: 0,10,20,30,40,...,100

print("Aléatoire entier: ", aleatoire1)
print("Aléatoire décimal: ", aleatoire2)
print("Aléatoire entier: ", aleatoire3)
print("Aléatoire entier: ", aleatoire4)