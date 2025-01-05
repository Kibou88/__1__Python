# Utilisation Enumerate avec un dico
# - Apprenre à utiliser Enumerate avec un dico
#-------------------------------------

dic = {
    'Utilisateur1': 'John',
    'Utilisateur2': 'Paul',
    'Utilisateur3': 'Julie'
}

for i, (cle, valeur) in enumerate(dic.items()):
    print(i, cle, valeur)
print("-------------------")
# Index de début à 1
for i, (cle, valeur) in enumerate(dic.items(), 1):
    print(i, cle, valeur)