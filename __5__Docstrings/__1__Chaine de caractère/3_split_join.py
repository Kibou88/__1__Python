# Manipuler les chaines de caractères part 3
# - Séparer une chaîne de caractère et les récupérer en liste
# - Réunir les éléments d'une liste et les mettre dans une chaîne de caractère
##########################################

def string_split(test):
    """Fonction pour séparer une chaîne de caractère et les récupérer en liste"""
    test_liste = test.split(", ") # Séparation de la virgule ET l'espace pour récupérer que le mot voulu
    print("Voici la liste splité: ", test_liste)

def string_join(test_2):
    """Fonction pour réunir les éléments d'une liste et les mettre dans une chaîne de caractère"""
    test_2_liste = " ".join(test_2) # Réunion de chaque élément de la liste séparé par  un espace
    print("Voici la nouvelle liste jointé: ", test_2_liste)

if __name__ == "__main__":
    test = "1, 2, 3, 4, 5"
    test_2 = ["Bonjour", "tout", "le", "monde"]

    string_split(test)
    string_join(test_2)