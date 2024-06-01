# Classes: Les bases
# -Apprendre les bases des classes
##################################

class Voiture:
    #Attributs de classe
    couleur="rouge"
    voiture_crees=0

    def __init__(self,marque): #self correspond à notre instance
        #Attributs d'instance
        Voiture.voiture_crees += 1 #A chaque instance, la variable prends +1
        self.marque = marque


print(Voiture.couleur)#Affiche l'attribut couleur de la classe Voiture

#Création d'instance
voiture_01=Voiture("Porsche")
voiture_02=Voiture("Lambo")
print(voiture_01.marque)

#Modifier la valeur d'un attribut de classe
Voiture.couleur="bleu" #Modifie l'attribut couleur
print(voiture_01.couleur)
print(voiture_02.couleur)
voiture_02.marque="Peugeot" #Modifie l'attribut marque que pour l'instance voiture_02
print(voiture_01.marque)
print(voiture_02.marque)
print(Voiture.voiture_crees) #Valeur = 2

