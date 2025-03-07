# Projet: Calculatrice basique
# - Permet de faire des additions, soustractions, multiplications et divisions
# PROJECT DONE
##############################################################################

def main():
    print("Choisir le type d'opération:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division /!\Mettre la 2nde valeur SUPERIEUR à 0 /!\ ")
    user_choice = input("Quel est votre choix: ")

    if not user_choice.isdigit(): # Si il n'y a pas que des chiffres, on recommence
        print("Il n'y a pas que des chiffres. Recommencer")
        quit()

    number_1 = int(input("Entrez le nombre 1: "))
    number_2 = int(input("Entrez le nombre 2: "))

    match user_choice:
        case "1":
            resultat = number_1 + number_2
            print(f"Le nombre 1 {number_1} + nombre 2 {number_2} est égale à {resultat}")
        case "2":
            resultat = number_1 - number_2
            print("Le nombre 1 {} - nombre 2 {} est égale à {}".format(number_1,number_2,resultat))
        case "3":
            resultat = number_1 * number_2
            print("Le nombre 1 {number1} * nombre 2 {number2} est égale à {total}"
                  .format(number1=number_1,number2=number_2,total=resultat))
        case "4":
            resultat = number_1 / number_2
            print("Le nombre 1 {} / nombre 2 {} est égale à {}".format(number_1,number_2,resultat))

if __name__ == '__main__':
    while True:
        main()