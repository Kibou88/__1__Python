# Ecrire dans un fichier
# - Apprendre à écrire dans un fichier
#####################################

chemin = "fichier.txt"

# Paramètres:
# w: Pour écraser les données existantes
# a: POur ajouter les données à la suite des données existantes

with open(chemin, "a") as f:
    f.write("\nBonjour")