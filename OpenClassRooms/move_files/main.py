import shutil
import os

file_source = "C:/Users/Satoshi/Desktop/Code/Extraction_recette/Sucrée"
# file_destination = "Path/Of/Directory"

get_files = os.listdir(file_source)
print("Nombre de fichier: ", len(get_files))
# for g in get_files:
#     shutil.move(file_source + g, file_destination) #Déplace tout les fichiers d'un dossier vers un autre
