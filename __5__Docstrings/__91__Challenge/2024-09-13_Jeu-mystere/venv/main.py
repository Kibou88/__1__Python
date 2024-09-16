# main.py
# But:
# Contient la logique du code
# -----------------------------------
# Date de création: 2024-09-13
# Date de dernière modification: 2024-09-16
# ------------------------------------------
# version: 2.0
# - Création des méthodes "intro_number_try", "final_message", "difference_user_mystere"
# - Amélioration d'une mauvaise saisie utilisateur
# - Simplification du code avec l'ajout des nouvelles méthodes
#-------------------------------------------

# Appel des modules externes
import random

# Appel des modules internes
from constantes import YELLOW, GREEN, PURPLE, WHITE, RED


class Game_Mystere():
    """
    Classe contenant les méthodes pour la logique du jeu
    """

    def __init__(self):
        self.nombre_utilisateur = 0
        self.essais_restants = 0
        self.nombre_essais = 0
        self.nombre_mystere = random.randint(1, 100)

    def intro_number_try(self):
        """
        Affiche le message du début +  nombre d'essais choisis par l'utilisateur
        :return:
        """
        print("Bienvenue dans le jeu Le Nombre Mystère\n")
        self.nombre_essais = int(input("Veuillez choisir le nombre d'essai maximum: "))
        self.essais_restants = self.nombre_essais

    def bigger(self):
        """
        Indique au joueur que le nombre mystère est plus grand
        :return:
        (int): Nombre d'essais restants
        """
        print(f"\nLe nombre mystère est plus grand\n")
        self.essais_restants -= 1

    def smaller(self):
        """
        Indique au joueur que le nombre mystère est plus petit
        :return:
        (int): Nombre d'essais restants
        """
        print(f"\nLe nombre mystère est plus petit\n")
        self.essais_restants -= 1

    def final_message(self):
        """
        Message si l'utilisateur a trouvé le nombre ou si il a perdu
        :return:
        (bool): Renvoie la valeur True pour quitter le jeu
        """
        if self.essais_restants == 0:
            print(f"{RED}PERDU, le nombre mystère était {self.nombre_mystere}!!{WHITE}")
        elif self.nombre_mystere == self.nombre_utilisateur:
            print(f"{GREEN}Bravo, vous avez trouvé le nombre mystère!!{WHITE}")

        return True

    def difference_user_mystere(self):
        """
        Compare la valeur de l'utilisateur et le nombre mystère
        :return:
        Affiche le message approprié pour aiguiller l'utilisateur
        """
        if self.nombre_mystere > self.nombre_utilisateur:
            return jeu_mystere.bigger()
        elif self.nombre_mystere < self.nombre_utilisateur:
            return jeu_mystere.smaller()


    def user_try(self):
        """
        Indique au joueur que le nombre d'essais restants, et demande un nouvel essai
        :return:
        (int): Nombre inscrit par le joueur
        """
        print(f"\nEssai possible: {self.essais_restants}/{self.nombre_essais}")
        if self.essais_restants == 1:
            print(f"{PURPLE}DERNIER ESSAI:")
        return int(input(f"Veuillez entre un nombre entre 1 et 100: {WHITE}"))

    def error_input(self):
        """
        Indique au joueur que son nombre n'est pas compris entre 1 et 100 ou que ce n'est pas un nombre
        :return:
        """
        if self.nombre_utilisateur < 1 or self.nombre_utilisateur > 100:
            print(f"{YELLOW}ERREUR!! Veuillez écrire un nombre entre 1 et 100....{WHITE}")
            return True


if __name__ == "__main__":
    jeu_mystere = Game_Mystere()
    jeu_mystere.intro_number_try()

    while jeu_mystere.essais_restants > 0 and jeu_mystere.nombre_utilisateur != jeu_mystere.nombre_mystere:

        # Message d'erreur si l'utilisateur n'écrit pas des nombres
        try:
            jeu_mystere.nombre_utilisateur = jeu_mystere.user_try()
        except ValueError:
            print(f"{RED}Veuillez saisir un nombre!!{WHITE}")
            continue

        if jeu_mystere.error_input(): # Erreur de saisie. La boucle s'arrête et l'utilisateur ressaisi un nouveau nombre
            continue

        jeu_mystere.difference_user_mystere()

        if jeu_mystere.final_message():
            break



