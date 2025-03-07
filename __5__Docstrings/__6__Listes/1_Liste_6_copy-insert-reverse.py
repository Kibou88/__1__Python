# Les listes
# - Copier une liste
# - Insérer un élément
# - Inverser la liste
#################################################

liste_origin = ["Coucou", "Bonjour", True]

# Copier une liste
liste_copy = liste_origin.copy()
print(liste_copy)

# Insérer un élément dans une liste
# # insert(index, item)
liste_origin.insert(2, "Au revoir")
print(liste_origin)

# Inverser une liste
liste_origin.reverse()
print(liste_origin)