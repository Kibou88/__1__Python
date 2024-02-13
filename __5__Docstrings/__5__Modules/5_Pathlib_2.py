# Module Pathlib part 2
# - Apprendre le fonctionnement du module Pathlib
# - Gestion des fichiers
#################################################
from pathlib import Path

chemin = Path.cwd()
p = chemin / "dossier3" / "main" #Concaténation de dossier/fichier
print("Chemin concaténer: ", p)
p.mkdir(exist_ok=True, parents=True) # Créer le chemin
p = p / "readme.txt"
p.touch() # Créer le fichier texte
# p.unlink() # Supprime le fichier texte

p.write_text("Bonjour") # Ecrire dans le fichier texte
print(p.read_text()) # Lire dans le fichier texte
