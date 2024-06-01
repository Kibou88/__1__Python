# Classes: L'héritage
# -Comprendre et apprendre l'héritage
##################################################
"""
Eviter de répéter des lignes de codes en Python
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
        Utilisateur.__init__(self, nom, prenom) #Appelle de la méthode init de la classe parent


paul = Junior("Paul", "Durand")
paul.afficher_projets()