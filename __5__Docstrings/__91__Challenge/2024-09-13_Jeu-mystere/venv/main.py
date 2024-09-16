# main.py
# But:
# Contient la logique du code
# -----------------------------------
# Date de création: 2024-09-13
# Date de dernière modification: 2024-09-14
# ------------------------------------------
# version: 1.0
# -
#-------------------------------------------

# Appel des modules externes
import random

# Appel des modules internes
from constantes import YELLOW, GREEN, PURPLE, WHITE

# Variables globales
NOMBRE_MYSTERE = random.randint(1,100)


class Game_Mystere():
    """
    Classe contenant les méthodes pour la logique du jeu
    """

    def __init__(self, nombre_essais, essais_restants):
        self.nombres_essais = nombre_essais
        self.essais_restants = essais_restants
        self.NOMBRE_MYSTERE = NOMBRE_MYSTERE

    def bigger(self):
        """
        Indique au joueur que le nombre mystère est plus grand
        :return:
        (int): Nombre d'essais restants
        """
        print(f"\nLe nombre mystère est plus grand\n")
        return self.essais_restants - 1

    def smaller(self):
        """
        Indique au joueur que le nombre mystère est plus petit
        :return:
        (int): Nombre d'essais restants
        """
        print(f"\nLe nombre mystère est plus petit\n")
        return self.essais_restants - 1

    def user_try(self):
        """
        Indique au joueur que le nombre d'essais restants, et demande un nouvel essai
        :return:
        (int): Nombre inscrit par le joueur
        """
        print(f"\nEssai possible: {essais_restants}/{nombre_essais}")
        if self.essais_restants == 1:
            print(f"{PURPLE}DERNIER ESSAI:")
        return int(input(f"Veuillez entre un nombre entre 1 et 100: {WHITE}"))

    def error_input(self):
        """
        Indique au joueur que son nombre n'est pas compris entre 1 et 100
        :return:
        """
        print(f"{YELLOW}ERREUR!! Veuillez écrire un nombre entre 1 et 100....{WHITE}")



if __name__ == "__main__":
    print("Bienvenue dans le jeu Le Nombre Mystère\n")
    nombre_essais = int(input("Veuillez choisir le nombre d'essai maximum: "))

    essais_restants = nombre_essais
    nombre_utilisateur = 0

    while essais_restants > 0 and nombre_utilisateur != NOMBRE_MYSTERE:
        jeu_mystere = Game_Mystere(nombre_essais, essais_restants)
        nombre_utilisateur = jeu_mystere.user_try()

        if nombre_utilisateur < 1 or nombre_utilisateur > 100 :
            jeu_mystere.error_input()
            continue

        if NOMBRE_MYSTERE > nombre_utilisateur:
            essais_restants = jeu_mystere.bigger()
        elif NOMBRE_MYSTERE < nombre_utilisateur:
            essais_restants = jeu_mystere.smaller()
        elif NOMBRE_MYSTERE == nombre_utilisateur:
            break

    print(f"{GREEN}Bravo, vous avez trouvé le nombre mystère!!{WHITE}")
