# Les listes part 3
# - Autres méthodes pour enlever des éléments d'une liste
##########################################################
employes = ["Carlos", "Max", "Martine", "Patrick", "Max"]

element = employes.pop(-1) # pop supprime l'élément dans la liste par rapport à l'indice entre ()
print(employes)
print(element)

employes.remove("Max") # Remove prends la valeur d'un élément
employes.remove("George") # Si l'élément est absent de la liste, il retourne une ValueError
print(employes)

employes.clear() # Vide la liste
print(employes)