# Any & All
# - Apprendre à utiliser Any et All
#-----------------------------------
"""
Permet de vérifier si au moins un ou tout les éléments d'un itérable sont vraies
"""
exemple = any([False, True, False, False])
print(exemple)

exemple1 = all([False, True, False, False])
print(exemple1)

exemple3 = any([True, True, True, True])
print(exemple3)

exemple4 = all([False, False, False, False])
print(exemple4)
#---------------------------------------------------
# Avec Any
ages_invites = [5, 10, 15, 20]

autorisation = any(a >= 18 for a in ages_invites)
print(autorisation)

autorisation2 = any(a >= 21 for a in ages_invites)
print(autorisation2)

# Avec All
ages_invites2 = [19, 20, 21, 22]

autorisation3 = all(a >= 18 for a in ages_invites2)
print(autorisation3)

autorisation4 = all(a >= 21 for a in ages_invites2)
print(autorisation4)