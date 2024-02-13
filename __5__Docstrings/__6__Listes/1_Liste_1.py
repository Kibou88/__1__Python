# Les listes part 1
# - Que mettre dans une liste
# - Apprendre à convertir range en list
# - Apprendre à utiliser les tuples
########################################
# Les listes sont des objets mutables!!
liste = [] #Initialisation d'une liste vierge
liste = [50,"Coucou", True] #Accepte n'importe tout type de variable
print(liste)

list_range=list(range(-12,3,3)) #range(x,y,z)
# x: valeur au départ (inclus)
# y: valeur de fin (non inclus, s'arrête à y - 1)
# z: pas
print(list_range)

liste_tuple = tuple(liste) # Convertit la liste en tuple
print(liste_tuple)