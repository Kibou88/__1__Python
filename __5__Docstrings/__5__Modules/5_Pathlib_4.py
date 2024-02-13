# Module Pathlib part 4
# - Apprendre le fonctionnement du module Pathlib
# - Ajouter un suffixe à un nom de fichier
# - Trier des fichiers
#######################################################################
from pathlib import Path
from pprint import pprint

# p = Path.home() / "Pictures" / "Screenshots" / "beta.png"
# p1 = p.parent / p.stem # Récupère le chemin + nom du fichier
# print(p1)
#
# p2 = p.parent / (p.stem + "-lower" + p.suffix) # Ajoute "-lower" entre le nom et l'extension
# print(p2)
# p2.rename(p) # Renomme le fichier.
# p2.rename(p)
# p: Chemin + nom origine du fichier
# p2: Chemin + nouveau nom du fichier

#///////////////////////////////////////////////////////////////
dirs = {".pdf": "Documents",
        ".mp4": "Vidéos",
        ".zip": "Archives",
        ".xlsm": "Excel macro",
        ".docx": "Word",
        ".png": "Images"} # Dico pour répertorié les fichiers en fonction de leurs extensions

tri_dir = Path.cwd() / "tri" # Répertoire où se trouve le dossier de tri à faire
files = [f for f in tri_dir.iterdir() if f.is_file()] # Répertorie SEULEMENT tous les fichiers présents dans le dossier
for f in files:
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    #dirs.get(param1, param2): param1: cherche le suffixe dans le dico
    #                          param2: Si aucun suffixe trouvé, prépare la création du dossier "Autres"
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name) # Va déplacer le fichier dans le dossier correspondant à son extension