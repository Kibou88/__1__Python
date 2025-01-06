# Compréhension liste
# - Apprendre à utiliser les compréhensions de liste
#####################################################
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
"""
[expression boucle for condition]
"""
liste2 = [i*2 for i in liste]
print(liste2)

"""
[expression boucle for condition if condition]
"""
liste3 = [i+2 for i in liste if i > 0]
print(liste3)

"""
[expression if condition else expression boucle for condition ]
"""
liste3 = [i+2 if i > 0 else i-2 for i in liste]
print(liste3)