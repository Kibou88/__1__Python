# Classes: Databaclasses
# -Comprendre le module Dataclasse
# -Module sur Python3.7/!\
##################################
from dataclasses import dataclass
from typing import ClassVar

#Décorateur dataclass
@dataclass
class User:
    #Attribut de classe
    c: ClassVar[int] = "50 "
    #Entre [] type de données

    #Attribut d'instance
    first_name: str #Annotation de type. Sers d'indicateur, n'empêche pas l'init de se faire
    last_name: str = "" #Paramètre par défaut

    def __post_init__(self): #Méthode qui s'éxécute juste après l'init
        self.full_name = f"{self.first_name} {self.last_name}"


#Ce code équivaut à la partie en dessous
class User_2:
    def __init__(self, first_name2: str, last_name2: str):
        self.first_name2 = first_name2
        self.Last_name2 = last_name2

patrick = User(first_name="Patrick", last_name="Smith")
print(repr(patrick)) #Représentation de la classe avec repr()
print(patrick.full_name)
paul = User(first_name="Paul")
print(repr(paul)) #Représentation de la classe avec repr()