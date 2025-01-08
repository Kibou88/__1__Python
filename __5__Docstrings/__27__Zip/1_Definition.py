# Fonction Zip
# - Apprendre à utiliser la fonction zip
#----------------------------------------
liste_1 = [1, 2, 3]
liste_2 = ['un', 'deux', 'trois', 'quatre']
liste_3 = ['Julien', 'Marie']

# La fonction Zip va combiner plusieurs listes ensembles sous forme de tuple
# va s'arrêter à l'itérateur le plus court (=> liste la plus courte)
resultat1 = list(zip(liste_1, liste_2))
print(resultat1)

resultat2 = list(zip(liste_1, liste_2, liste_3))
print(resultat2)