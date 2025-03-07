# Utilisation Enumerate avec une liste
# - Apprenre à utiliser Enumerate avec une liste
#-------------------------------------

liste = ["Bonjour", "tout", "le", "monde"]

for i, mot in enumerate(liste):
    print(i, mot)
print("-------------------")
# Index de début à 1
for i, mot in enumerate(liste, 1):
    print(i, mot)