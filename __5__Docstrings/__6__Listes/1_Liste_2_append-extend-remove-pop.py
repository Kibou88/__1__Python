# Les listes part 2
# - Ajouter/Retirer des éléments d'une liste
# - Récupérer un élément dans une liste
# - Slices
# - Autres méthodes
#################################################

liste=["Coucou", "Bonjour", True]
print(liste)
liste.append(5) #Ajoute une valeur à la fois
print("New liste:", liste)
liste.extend([10,20,30]) #Ajoute plusieurs éléments dans la liste
print("New liste 2:", liste)
liste.remove(5) #Enlève la 1ère occurence d'une liste! Si plusieurs éléments, refaire le remove
print("New liste 3:", liste)
removed = liste.pop(1) # Pop retire l'élément par son index mais on peut le stocker dans une variable
print("L'élément retiré est: ", removed)

print("Affiche l'élément de l'indice 1:",liste[1]) #L'indice de gauche à droite commence par 0
print("Affiche l'élément de l'indice -2:", liste[-2]) #L'indice de droite à gauche commence par -1

print(liste[0:4:2]) #Récupère les éléments de l'indice 0 à 3 par pas 2
print(liste[:-1]) #S'arrête à l'avant dernier indice
print(liste[::2]) #Prendre un élément sur 2