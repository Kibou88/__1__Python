# Module Pathlib part 3
# - Apprendre le fonctionnement du module Pathlib
# - Scanner des dossiers et récupérer tout les fichiers/dossiers dedans
#######################################################################
from pathlib import Path
from pprint import pprint

Path.home().iterdir() #Renvoie un objet itérateur

for f in Path.home().iterdir():
    print(f.name) # Afficher le nom du fichier ou dossier y compris les dossiers/fichiers cachés
# Comprehension list: [f.name for f in Path.home().iterdir()]
pprint([f for f in Path.home().iterdir() if f.is_dir()]) # Retourne tout les dossiers
print("\n")
pprint([f for f in Path.home().iterdir() if f.is_file()]) # Retourne tout les fichiers

# rglob agit de façon récursive
p = Path.home() / "Pictures" / "Screenshots"
print(p)
pprint([f.name for f in p.glob("*.png")]) # Permet d'afficher la liste des png dans le dossier actuel
# sous format comprehension list

pprint([f.name for f in p.rglob("*.png")]) # Permet d'afficher la liste des png dans le dossier actuel ET dans les
# sous-dossiers sous format comprehension list