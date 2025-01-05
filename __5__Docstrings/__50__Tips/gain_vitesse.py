# Gain vitesse
# - Différences entre objets muables et immuables
# - Analyse de performance
########################################
import time

a = time.time()
chaine = ""
for i in range(99999):
    chaine += str(i)
b = time.time()

print(f"Fin du programme: {b - a} sec") # environ 12 sec

a = time.time()
liste = []
chaine = ""
for i in range(99999):
    liste.append(str(i))
chaine = "".join(liste)

b = time.time()
print(f"Fin du programme: {b - a} sec") # environ 0.01 sec
