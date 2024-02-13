# Utilisation du JSON
# - Apprendre à lire/écrire dans un JSON
########################################
import json

fichier = "settings.json"
"""
with open(fichier, 'r') as f: # Ouvrir le fichier en lecture
    settings = json.load(f) #Récupère le JSON et le stocke
print(settings) #Afficher le JSON

settings["fontsize"] = 20 # Modification de la valeur de la clé

with open(fichier,'w') as f: # Ecrire dans le fichier JSON
    json.dump(settings, f, indent=4) # Ecrit dans le JSON avec une indentation de 4
    # /!\ ECRASE LES DONNEES DEJA EXISTENT
"""
with open(fichier, 'r') as f:
    donnees = json.load(f)
print(type(donnees))
donnees["Pèche"]=30

with open(fichier,'w') as f:
    json.dump(donnees, f, indent=4, ensure_ascii=False)
    # ensure_ascii=False => Permet de mettre les accents sur les clés