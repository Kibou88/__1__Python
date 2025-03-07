# Classes: Fonction Super
# -Comprendre et apprendre sur la fonction Super
##################################################

"""

"""
projets = ["pr_GameOfThrones", "HarryPotter", "pr_Avenger"]

class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f'Utilisateur {self.nom} {self.prenom}'

    def afficher_projets(self):
        for projet in projets:
            print(projet)

class Junior(Utilisateur):
    #Classe héritée de la classe Utilisateur
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom) #Appelle de la méthode init de la classe parent
        #Avec la fonction Super, retirer le 'self' entre les () __init__


paul = Junior("Paul", "Durand")
paul.afficher_projets()