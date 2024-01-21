def welcome_game(): # Affiche le message de bienvenue et renvoie ce que veux l'utlisateur
    import os
    os.system("clear") # Vide tout ce qui était avant
    print("Bienvenue dans le pendu")
    print("Etes-vous pret? ")
    print("Oui pour commencer, exit pour quitter le jeu:")
    partie = input()

    return partie

def initialize_counter(): # Initialise les compteurs coups et mort
    coups = 1
    mort = 11
    return coups, mort