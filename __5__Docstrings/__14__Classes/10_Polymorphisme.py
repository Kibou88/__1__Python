# Classes: Le polymorphisme
# -Comprendre et apprendre sur le polymorphisme
##################################################

"""
Concept associé au classe qui indique qu'on doit pouvoir utiliser des méthodes d'une même façon sur
toutes les entités
"""
class Vehicle:
    def avance(self):
        print("Le véhicule démarre")

class Voiture(Vehicle):
    def avance(self):
        super().avance()
        print("La voiture roule")

class Avion(Vehicle):
    def avance(self):
        super().avance()
        print("L'avion vol")

v = Voiture()
a = Avion()
v.avance()
a.avance()