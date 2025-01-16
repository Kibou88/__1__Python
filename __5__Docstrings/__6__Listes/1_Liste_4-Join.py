# Liste 4 join
# - utilisation de filter avec join
#----------------------------------------
tags_photo = ['vacances', 'juin', 'italie', None]

nom_fichier = '_'.join(filter(None, tags_photo))
print(nom_fichier)

nom_fichier2 = '_'.join(tags_photo) # Retourne un TypeError à cause de None
print(nom_fichier2)