# Module Pathlib
# - Apprendre le fonctionnement du module Pathlib
#################################################
from pathlib import Path

print("Dossier utilisateur: ", Path.home()) # Retourne le dossier utilisateur

print("Dossier courant: ", Path.cwd()) # Retourne le dossier courant
#cwd: Current Working Directory

chemin = Path("C:\\Users\\Satoshi\\Desktop\\Code\\__1__Entrainement_Python\\__5__Docstrings\\__5__Modules")
print("Chemin: ", chemin)
print("Dossier parent de chemin: ", chemin.parent) # Retourne le dossier parent de chemin
print("Dossier parentx2 de chemin: ", chemin.parent.parent) # Retourne le dossier parent de chemin puis de Docstring

chemin = Path.cwd()
p = chemin / "documents" / "main.py" #Concaténation de dossier/fichier
print("Nouveau chemin concaténer: ", p)
p1 = chemin.joinpath("documents", "main.py") # Même résultat qu'au dessus
print("Nouveau chemin concaténer 2: ", p1)

print("Récupérer le suffixe: ", p1.suffix)