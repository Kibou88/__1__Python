# Créer une nouvelle liste
#------------------------------

liste = [1, 2, 3]
liste_copie = liste # Même liste en mémoire

liste.append(5)

print(liste)
print(liste_copie)
print()
#---------------------------
liste = [1, 2, 3]
liste_copie = liste[:] # Utilisation des slices

liste.append(5)

print(liste)
print(liste_copie)
print()
#----------------------------
liste = [1, 2, 3]
liste_copie = list(liste) # Convertion la liste d'origine en liste

liste.append(5)

print(liste)
print(liste_copie)
print()
#----------------------------
liste = [1, 2, 3]
liste_copie = liste.copy() # Copie la liste

liste.append(5)

print(liste)
print(liste_copie)
print()