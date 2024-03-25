# Exercice Réduction prix
# - But: Créer un nouveau dictionnaire avec les prix réduits
####################################################################
produits = [
    {"nom": "Ordinateur", "prix": 1000},
    {"nom": "Smartphone", "prix": 500},
    {"nom": "Tablette", "prix": 300},
]

reductions={}
for produit in produits:
    print(produit)
    price=0
    for key, value in produit.items():
        if key=="nom":
            nom=value
        elif key=="prix":
            price=value*0.9
        reductions[nom]=price
print("Ma solution: ", reductions)
############################################
produits = [
    {"nom": "Ordinateur", "prix": 1000},
    {"nom": "Smartphone", "prix": 500},
    {"nom": "Tablette", "prix": 300},
]

reductions = {}

for produit in produits:
    reductions[produit["nom"]] = produit["prix"] * 0.9
print("Solution cours: ", reductions)

langage = "Python"
chaine="Vous êtes bien en train d'apprendre le langage Python"
resultat=chaine if langage=="Python" else ""
print(resultat)