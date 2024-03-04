# Actions dictionnaires
# - Répertorie la liste des actions possibles sur un dico
##########################################################
d = {
    0:{"prenom": "Paul",
       "profession": "Ingénieur",
       "ville": "Paris"},
    1:{"prenom": "Julie",
       "profession": "Architecte",
       "ville": "Marseille"},
    2:{"prenom": "Pierre",
       "profession": "Plombier",
       "ville": "Nantes"}
}

# Modifier la valeur d'une clé
d[0]["prenom"]="Toto"
print(d[0]["prenom"])

# Ajouter et supprimer une clé
d[0]["age"]=30 #/!\Si la clé existe déjà la valeur de la clé sera écrasé
print(d[0])

del d[0]["age"] # Supprimer la clé!
print(d[0])
#Pour éviter les erreurs utiliser la syntaxe ci-dessous:
if "age" in d:
    del d["age"]

# Boucler sur un dictionnaire
print(d[0].keys()) # Permet d'afficher les clés du dictionaire de l'id 0
print(d[0].values()) # Permet d'afficher les valeurs du dictionnaire de l'id 0
print(d[1].items()) # Permet d'afficher une liste de tuple contenant clé,valeur de l'id 1