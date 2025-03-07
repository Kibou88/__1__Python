# Compréhension de liste avec 2 boucles for
#-------------------------------------------
liste_finale = []
for a in range(10):
    for b in range(2):
        liste_finale.append((a, b))
print(liste_finale)

liste_finale2 = [(a,b) for a in range(10) for b in range(2)]
print(liste_finale2)