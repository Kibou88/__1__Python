# Manipuler les chaines de caractères part 1
# - Tout mettre en minuscule
# - Tout mettre en majuscule
# - 1ere lettre en majuscule
# - 1ere lettre de chaque mot en majuscule
##########################################

def string_lower(test):
    """Fonction pour mettre toutes les lettres en minuscule"""
    print("Lettres en minuscules: ",test.lower())

def string_upper(test):
    """Fonction pour mettre toutes les lettres en majuscule"""
    print("Lettres en minuscules: ", test.upper())

def string_capitalize(test):
    """Fonction pour mettre la 1ère lettre de la chaîne en majuscule"""
    print("Lettres en minuscules: ", test.capitalize())

def string_title(test):
    """Fonction pour mettre toutes les 1ères lettres en majuscule"""
    print("Lettres en minuscules: ", test.title())

if __name__ == '__main__':
    test = "BonJouR ToUt le moNDe"
    print("Chaîne de base: ", test)
    string_lower(test)
    string_upper(test)
    string_capitalize(test)
    string_title(test)