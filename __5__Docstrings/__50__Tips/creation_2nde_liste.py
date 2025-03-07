# Création 2nde liste
# - Eviter le piège lors de la création d'une liste
#--------------------------------------------------
liste = [1, 2, 3, 4, 5]
liste_double = []
for i in liste:
    liste_double.append(i*2)

# Les 2 listes ont la même case mémoire => si 1 liste change => l'autre aussi
liste = liste_double
print(f'id liste {id(liste)}')
print(f'id liste {id(liste_double)}')

liste_double.append(7)
print(f'liste {liste}')
print(f'liste_double {liste_double}\n\n')
#------------------------------------------------------
liste = [1, 2, 3, 4, 5]
liste_double = []
for i in liste:
    liste_double.append(i*2)

# Les 2 listes ont un espace mémoire différent => si 1 liste change => l'autre non
liste = liste_double[:]
# liste = list(liste_double)
print(f'id liste {id(liste)}')
print(f'id liste {id(liste_double)}')

liste_double.append(7)
print(f'liste {liste}')
print(f'liste_double {liste_double}')