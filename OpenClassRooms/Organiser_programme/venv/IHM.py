def IHM_all():
    """Fonctions pour réunir toutes les fonctions IHM"""
    choice_validate = "n" # Le choix n'est pas valide

    while choice_validate != "y":
        choice = welcome_message()
        choice_validate = message_user_choice(choice, choice_validate)
        print("\n")
        choice_validate = valid_choice(choice, choice_validate)
    return choice


def welcome_message():
    """Fonction pour afficher le message de bienvenue, la liste des choix et le choix utilisateur"""
    import os

    os.system("cls")
    print("Bienvenue dans votre bibliothèque de films!")
    print("Que voulez-vous faire?")
    print("1.Voir la liste des films par nom")
    print("2.Voir la liste des films par date de création")
    print("3.Voir la liste des films par type")
    print("4.Choisir un film au hasard")
    print("5.Savoir quel(s) film(s) sont chez des amis (si oui, lesquels)")
    print("6.Exit (commande '6' ou 'exit')")
    return input("Quel est ton choix? ")

def message_user_choice(choice, choice_validate):
    """Fonction pour montrer à l'utilisateur quel choix a été fait et si il veut confirmer"""
    import time
    match choice.lower():
        case "1":
            print("Vous avez choisis de voir la liste des films par noms")
        case "2":
            print("Vous avez choisis de voir la liste des films par date de création")
        case "3":
            print("Vous avez choisis de voir la liste des films par type")
        case "4":
            print("Vous avez demandé à choisir un film au hasard")
        case "5":
            print("Vous avez demandés à voir si des films sont chez des amis")
        case "6":
            print("Voulez-vous quitter le programme?")
        case "exit":
            print("Voulez-vous quitter le programme?")
        case _:
            print("Ce n'est pas un choix valide")
            print("Recommencez")
            time.sleep(1)
            choice_validate = "0"
            return choice_validate

def valid_choice(choice, choice_validate):
    """Fonction pour demander à l'utilisateur si il veut valider son choix"""
    if choice_validate == "0":
        choice_validate = "n"
    else:
        choice_validate = input("Est-ce le bon choix? y pour oui et n pour non: ")
        if choice_validate == "y" and (choice == "6" or choice == "exit"):
            exit()
    return choice_validate