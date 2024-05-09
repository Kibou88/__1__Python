# Classes: Les bases
# -Apprendre les bases des classes
##################################

class Voiture:
    #Attributs de la classe
    marque = "Lamborghini"
    couleur = "rouge"

print(Voiture.marque) #Affiche l'attribut marque de la classe Voiture
print(Voiture.couleur)

#Création d'instance
voiture_01=Voiture()
voiture_02=Voiture()
print(voiture_01.marque)