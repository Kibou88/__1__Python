# Module Pathlib part 1
# - Apprendre le fonctionnement du module Pathlib
# - Gestion des dossiers
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
p = chemin / "dossier2" / "main.py" #Concaténation de dossier/fichier
print("Nouveau chemin concaténer: ", p)
p1 = chemin.joinpath("documents", "main") # Même résultat qu'au dessus
print("Nouveau chemin concaténer 2: ", p1)

print(p.name) # Récupère le nom + extension
print(p.stem) # Récupère le nom du fichier
print(p.suffix) # Récupère l'extension
print(p.suffixes) # Récupère les extensions
print(p.parts) # Récupère les différentes parties du chemin
print(p.exists()) # Vérifie si il existe
print(p.is_dir()) # Vérifie si c'est un dossier
print(p.is_file()) # Vérifie si c'est un fichier

p1.mkdir(exist_ok=True, parents=True) # Créer le dossier
#exist_ok=True: Ne retourne pas d'erreur si le dossier existe déjà
#parents=True: Créer une hiérachie de dossier en une seule fois

p1=p1.parent
p1.rmdir() # Supprime un dossier SEULEMENT SI LE DOSSIER EST VIDE!!!
# Utiliser shutil.rmtree(p) pour supprimer un ensemble de dossier non vide