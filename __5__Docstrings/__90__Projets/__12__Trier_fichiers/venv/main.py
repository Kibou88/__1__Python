"""
Projet: Trier fichiers
---------------------
main.py
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

from constantes.file_format import PICTURE_FORMAT
from constantes.constantes import DICO_MOIS
from path_creation import Path_Creation

user_path = Path(input("Entrer le chemin dans lequel se trouve les photos a trier: "))

# => Gestion d'erreur à rajouter
# if platform.system() == "Windows" and not "\\\\" in user_path:
    # Ajoute \\ au chemin utilisateur
    # user_path = Path(user_path.replace("\\", "\\\\"))

# ------- Vérifier la présence des fichiers ------- OK
# Récupère le nom + extension du fichier
files_found = [x for x in user_path.iterdir() if (x.is_file() and x.suffix.lower() in PICTURE_FORMAT)]
# print(files_found)

# ------- Récupérer les métadonnées ------- OK
for file in files_found:
    try:
        file_path = Path_Creation(user_path, DICO_MOIS).file_path(file)
        file_size = os.path.getsize(file_path) # Récupère la taille du fichier
        # file_creation_time = time.localtime(os.path.getctime(file_path)) # Récupérer la date de la création du fichier
        file_creation_time = time.localtime(os.path.getmtime(file_path))  # Récupérer la date de modification du fichier
        file_creation_year = file_creation_time.tm_year # Année
        file_creation_month = file_creation_time.tm_mon # Mois
        # print(file_creation_month)

        path_year_month = Path_Creation(user_path, DICO_MOIS).path_year_month(file_creation_year, file_creation_month)

        # ------- Déplacement du fichier dans le répertoire mois -------
        file.rename(path_year_month / file.name)
    except:
        with open("Log.txt", "a+") as f:
            f.write(f'Erreur avec le fichier {file}')