# Compréhension liste
# - Apprendre à utiliser les compréhensions de liste
#####################################################

liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = []
for i in liste:
    if i > 0:
        nombres_positifs.append(i)
print(nombres_positifs)

# équivalent en compréhension liste
"""
[resultat boucle for condition if  condition else]
"""
nombres_positifs2 = [i for i in liste if i > 0]
print(nombres_positifs2)
