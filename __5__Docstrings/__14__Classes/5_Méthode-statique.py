# Classes: Méthode statique
# -Comprendre et apprendre les méthodes statique
##################################################

"""
Les méthodes statiques n'ont pas besoin d'avoir de paramètres définis dans une classe
"""
class Voiture:
    voitures_crees=0

    def __init__(self, marque, vitesse, prix):
        Voiture.voitures_crees += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    @classmethod  # Décorateur pour indiquer la méthode de la classe
    def lamborghini(cls):  # Prends 1 seul argument: cls (classe) représente la classe (ici Voiture)
        return cls(marque="Lamborghini", vitesse=250, prix=2000000)  # Retourne une instance pré-enregistré de Voiture

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=200, prix=180000)

    @staticmethod
    def afficher_nombre_voitures(): #Retirer le self
        print(f'Vous avez {Voiture.voitures_crees} voitures dans votre garage')


lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
Voiture.afficher_nombre_voitures()