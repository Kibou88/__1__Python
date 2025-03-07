# Aplatir et supprimer doublon
#------------------------------------
"""
Aplatir pour supprimer des listes à l'intérieur d'une liste
i.e: [[1, 2, 3], 4] ==> [1, 2, 3, 4]
"""
ma_liste = [[1, 7, 3], [3, 4], [12, 1, 4, 8]]

ma_liste_aplatie = sum(ma_liste, [])
print(ma_liste_aplatie)

# Supprimer les doublons

ma_liste_sans_doublons = sorted(list(set(ma_liste_aplatie)))
print(ma_liste_sans_doublons)