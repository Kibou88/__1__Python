# Classes: La Surcharge
# -Comprendre et apprendre sur la Surcharge
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
        super().__init__(nom, prenom)

    def afficher_projets(self):
        #On vient écraser la méthode de la classe parent par celle-ci pour la classe enfant
        for projet in projets:
            if not projet.startswith("pr_"):
                print(projet)


paul = Junior("Paul", "Durand")
marc = Utilisateur("Marc", "Martin")
paul.afficher_projets()
marc.afficher_projets()