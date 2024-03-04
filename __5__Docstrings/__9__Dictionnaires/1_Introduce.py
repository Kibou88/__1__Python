# Introduce dictionnaire
# - Apprendre à utiliser les dico
#################################

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

print(d[0]["prenom"]) #Affiche le prenom avec l'id 0
#/!\Si la clé n'existe pas, il y aura une erreur /!\
try:
    print(d[0]["job"])
except KeyError:
    print("La clé 'job' n'existe pas")

print(d.get('prenom')) # Retourne 'NONE' si la clé n'existe pas
print(d.get('prenom',"La clé n'existe pas")) # Revient à faire le try-except