# Liste initiale
elements = ["arbre", "arbre", "(abricot)", "arbre", "((pêche))", "arbre", "banane"]

# Dictionnaire pour stocker les fruits et le nombre de parenthèses
fruits_dict = {}

# Liste des fruits possibles (pour vérifier si un élément est un fruit)
fruits_possibles = ["abricot", "pêche", "banane"]

# Parcourir la liste
for element in elements:
    for fruit in fruits_possibles:
        if fruit in element:
            fruits_dict[fruit] = element.count("(")

# Afficher le dictionnaire
print(("()"*5).join(elements))
print(fruits_dict)
