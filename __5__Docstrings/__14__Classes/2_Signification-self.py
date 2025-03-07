# Classes: Signigication Self
# -Comprendre le self
##################################

class Voiture:
    def __init__(self, marque, prix):
        self.marque = marque
        self.prix = prix

    def afficher_marque(self): # 'Self' fait passer les informations de l'instance dans la méthode
        print(f"La voiture est une {self.marque} coute {self.prix}")

voiture_01 = Voiture("Lamborghini", 50000) #Création de l'instance avec des données pour marque et prix
voiture_01.afficher_marque()