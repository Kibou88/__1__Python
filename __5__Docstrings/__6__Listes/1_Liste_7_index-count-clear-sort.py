# Les listes
# - Récupérer l'index d'un élément
# - Compte le nombre d'occurence de l'élément
# - Effacer une liste
#################################################

employes = ["Carlos", "Max", "Martine", "Patrick", "Max"]
resultat = employes.index("Max") # Récupère l'index où se trouve la 1er fois l'élément
count_name=employes.count("Max") # Compte le nombre d'occurence de l'élément

print(resultat)
print(count_name)

liste_tri=sorted(employes) # Permet de récupérer dans une variable la chaine trier
employes.sort()



employes.clear() # Efface les données de la liste
print(employes)