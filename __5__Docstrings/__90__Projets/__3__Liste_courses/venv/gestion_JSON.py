import json

FICHIER_COURSE="Liste_course.json"
def lire_liste():
    """Fonction pour lire la liste des courses dans le fichier"""
    with open(FICHIER_COURSE, 'r') as file_json:
        datas=json.load(file_json) #Récupère le JSON et le stocke
    # print(data) #Affiche le JSON
    return datas
    file_json.close()

def ecrire_liste(donnees):
    """Fonction pour écrire dans la liste des course, sauver dans le fichier"""
    data=lire_liste()
    data.append(donnees)
    with open(FICHIER_COURSE, 'w') as file_json:
        json.dump(data, file_json, indent=4, ensure_ascii=False)
        # ensure_ascii: Permet d'afficher les accents
    file_json.close()

def remove_data_liste(remove_data):
    """Fonction pour réécrire le fichier JSON avec l'élément en moins
    OU pour vider toute la liste"""
    with open(FICHIER_COURSE, 'w') as file_json:
        json.dump(remove_data, file_json, indent=4, ensure_ascii=False)
        # ensure_ascii: Permet d'afficher les accents
    file_json.close()
