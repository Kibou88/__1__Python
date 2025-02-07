# Classes: Méthodes de classe
# -Comprendre et apprendre les méthodes de classe
##################################################

class Voiture:
    def __init__(self, marque, vitesse, prix):
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    @classmethod #Décorateur pour indiquer la méthode de la classe
    def lamborghini(cls): #Prends 1 seul argument: cls (classe) représente la classe (ici Voiture)
        return cls(marque="Lamborghini", vitesse = 250, prix=2000000) #Retourne une instance pré-enregistré de Voiture

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=200, prix = 180000)

lambo = Voiture.lamborghini() #Création d'une instance
porsche = Voiture.porsche()
print(porsche.prix)