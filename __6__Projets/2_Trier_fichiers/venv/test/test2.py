
import os
import stat
import time
# Spécifiez le chemin du fichier
file_path = \
    'C:\\Users\\Satoshi\\Desktop\\Code\\__1__Entrainement_Python\\__5__Docstrings\\__90__Projets\\__12__Trier_fichiers\\venv\\A_dater.jpg'

# Obtenir la taille du fichier
file_size = os.path.getsize(file_path)
print(f"Taille du fichier : {file_size} octets")

# parent_path = file_path.os.path.parent

# Obtenir la date de création du fichier
creation_time = os.path.getctime(file_path)
print(f"Date de création : {creation_time}")

# Obtenir la date de dernière modification du fichier
modification_time = os.path.getmtime(file_path)
new_date = time.localtime(modification_time)
print(f"Date de dernière modification : {modification_time}")
print(f"Annee: {new_date.tm_year}")
print(f"Date de dernière modification : {new_date}")

# Obtenir les métadonnées du fichier
# file_stats = os.stat(file_path)

# Afficher les métadonnées détaillées
# print(f"Taille du fichier : {file_stats.st_size} octets")
# print(f"Date du dernier accès : {file_stats.st_atime}")
# print(f"Date de dernière modification : {file_stats.st_mtime}")
# print(f"Mode du fichier : {file_stats.st_mode}")