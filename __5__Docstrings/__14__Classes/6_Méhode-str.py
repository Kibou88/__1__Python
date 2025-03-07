# Classes: Méthode __str__
# -Comprendre et apprendre la méthode __str__
##################################################

class Voiture:

    def __init__(self, marque, vitesse, prix):
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    @classmethod  # Décorateur pour indiquer la méthode de la classe
    def lamborghini(cls):  # Prends 1 seul argument: cls (classe) représente la classe (ici Voiture)
        return cls(marque="Lamborghini", vitesse=250, prix=2000000)  # Retourne une instance pré-enregistré de Voiture

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=200, prix=180000)

    def __str__(self): #Pas mettre de print, mettre un return
        #Garder self pour afficher le texte par rapport à l'instance
        return f'Voiture de marque {self.marque} avec vitesse maximale de {self.vitesse}.'


lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
print(porsche) #Affiche le contenu de la méthode __str__