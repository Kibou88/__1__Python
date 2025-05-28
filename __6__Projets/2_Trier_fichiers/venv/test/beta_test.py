"""
Projet: Trier fichiers
---------------------
beta_test.py
But: Contient la logique du programme
--------------------------------
Date de création: 2025-05-10
Date de modification: 2025-05-11
--------------------------------
Version: 1.0
"""

import os
import platform
import time
from pathlib import Path

from file_format import PICTURE_FORMAT
from constantes import DICO_MOIS

user_path = Path(input("Entrer le chemin dans lequel se trouve les photos a trier: "))

# => Gestion d'erreur à rajouter
# if platform.system() == "Windows" and not "\\\\" in user_path:
    # Ajoute \\ au chemin utilisateur
    # user_path = Path(user_path.replace("\\", "\\\\"))

# ------- Vérifier la présence des fichiers ------- OK
# Récupère le nom + extension du fichier
files_found = [x for x in user_path.iterdir() if (x.is_file() and x.suffix.lower() in PICTURE_FORMAT)]
print(files_found)

# ------- Récupérer les métadonnées ------- OK
for file in files_found:
    file_path = user_path.joinpath(file) # Ajoute le fichier au path
    file_size = os.path.getsize(file_path) # Récupère la taille du fichier
    file_creation_time = time.localtime(os.path.getctime(file_path)) # Récupérer la date de la création du fichier
    file_creation_year = file_creation_time.tm_year # Année
    file_creation_month = file_creation_time.tm_mon # Mois

    folder_year = user_path.joinpath(str(file_creation_year))
    # ------- Vérification dossier année déjà existant ------- OK
    if not folder_year.exists():
        folder_year.mkdir(exist_ok=True, parents=True)
        print(f"Le dossier {folder_year} a ete cree")
    else:
        print(f"Le dossier {folder_year} est deja existant")

    # ------- Vérification dossier mois déjà existant ------- OK
    year_path = user_path.joinpath(str(file_creation_year)) # Chemin vers le dossier de l'année du
    folder_month = year_path.joinpath(DICO_MOIS.get(str(file_creation_month))) # Convertit le chiffre du mois en
    if not folder_month.exists():
        folder_month.mkdir(exist_ok=True, parents=True)
        print(f"Le dossier {folder_month} a ete cree")
    else:
        print(f"Le dossier {folder_month} est deja existant")

    # ------- Déplacement du fichier dans le répertoire mois -------
    file.rename(folder_month / file.name)