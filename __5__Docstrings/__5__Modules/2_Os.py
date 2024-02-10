# Module Os
# - Apprendre le fonctionnement du module Os
############################################
import os
# Sous Windows, mettre des "\\" OBLIGATOIREMENT
chemin = "C:\\Users\\Satoshi\\Desktop\\Code\\__1__Entrainement_Python\\__5__Docstrings\\__5__Modules"
dossier = os.path.join(chemin, "dossier", "test") # Permet de gérer automatiquement les slash sous Windows, Linux, Mac
dossier2 = os.path.join(chemin, "dossier2")
print(dossier)

if not os.path.exists(dossier): # Si le dossier n'existe pas
    os.makedirs(dossier) # Permet de créer un ensemble de dossiers qui n'existent pas
    # Renvoie une erreur si un dossier est déjà crée

os.makedirs(dossier, exist_ok=True) # Permet de faire le même test qu'au dessus
if not os.path.exists(dossier2):
    os.mkdir(dossier2) # Permet de créer un dossier
#----------------------------------------------
if os.path.exists(dossier): # Même inconvénient que makedirs ou mkdir
    os.removedirs(dossier) # Permet de supprimer un dossier
    print("Dossier supprimé: ",dossier)