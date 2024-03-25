# Fonctions part 1
# - Apprendre à gérer une fonction avec valeur retour
#####################################################

def retourne_moi_cinq():
    return 5

def affiche(message="Default"): # Définit une valeur par défaut au paramètre
    print(message)

a = retourne_moi_cinq()
print(a)

affiche("Bonjour") # Donne à la fonction un argument
affiche()
#########################################################
def exemple():
    b=5 #Espace local seulement disponible pour la fonction

a=6 #Variable globale

