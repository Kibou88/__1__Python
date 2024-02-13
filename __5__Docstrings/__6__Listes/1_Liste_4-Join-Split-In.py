# Les listes part 4
# - Joindre les éléments d'une liste
# - Créer une liste à partir d'une chaine de caractère
# - Les opérateurs d'appartenances "in" et "not in"
#######################################################
liste = ["Python", "est", "un", "language", "de", "programmation"]
resultat = " ".join(liste) #avant JOIN, mettre le caractère souhaité
print(resultat)

liste2 = resultat.split(" ") # Par défaut, SPLIT utilise l'espace!!
print(liste2)

liste3=list(range(0,10,2))

if 4 in liste3:
    print("La valeur 4 est dans la liste")
if 5 not in liste3:
    print("La valeur 5 n'est pas dans la liste")