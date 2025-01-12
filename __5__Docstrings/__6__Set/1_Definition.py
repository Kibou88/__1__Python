# Set
# - Apprendre à utiliser les sets
#---------------------------------------
"""
les éléments d'un set sont immuables (une liste est muable)
pas de doublon
"""
mon_set = {1, 2, 3, 3, 'Julien', 'Julien', (255, 0, 0), (255, 0, 0)}
mon_set.add(5) # Ajouter un élément au set
mon_set.update(['Pierre', 6]) # Ajouter plusieurs éléments
mon_set.remove('Julien') # Retire un élément au set. Si pas l'élément retourne erreur
mon_set.discard('Jules') # Retire un élément au set si il existe, sinon pas d'erreur
print(mon_set)