# main.py
# But:
# Contient la logique du code
# -----------------------------------
# Date de création: 2024-09-13
# Date de dernière modification: 2024-09-18
# ------------------------------------------
# version: 3.0
# - Création des méthodes "intro_number_try", "final_message", "difference_user_mystere" (V2)
# - Amélioration d'une mauvaise saisie utilisateur (V2)
# - Simplification du code avec l'ajout des nouvelles méthodes (V2)
# - Appel de la classe Colors pour le changement de couleurs du texte (V3)
# - Suppresion des méthodes "intro_number_try" et "error_input"(V3)
# - Ajout opérateur ternaire dans "user_try" (V3)
# - Message d'accueil dans le constructeur "__init__" (V3)
# - Simplification de la méthode "difference_user_mystere" (V3)
# - Modification "Game_Mystere" by "GameMystere" (V4)
# - Passage des méthodes "user_try" et "difference_user_mystere" en privée (V4)
#-----------------------------------------------------------------------------------

# Appel des modules externes
import random

# Appel des modules internes
from constantes import Colors


class GameMystere:
    """
    Classe contenant les méthodes pour la logique du jeu
    """

    def __init__(self):
        self.nombre_utilisateur = 0
        self.essais_restants = 0
        self.nombre_essais = 0
        self.nombre_mystere = random.randint(1, 100)

        print("Bienvenue dans le jeu Le Nombre Mystère\n")
        self.nombre_essais = int(input("Veuillez choisir le nombre d'essai maximum: "))
        self.essais_restants = self.nombre_essais

    def __user_try(self):
        """
        Indique au joueur que le nombre d'essais restants, et vérifie la saisie utilisateur
        :return:
        (int): Nombre inscrit par le joueur
        """
        print(f"\nEssai possible: {self.essais_restants}/{self.nombre_essais}")

        print(f'{Colors.PURPLE}DERNIER ESSAI:' if self.essais_restants == 1 else '')

        try:
            self.nombre_utilisateur = int(input(f"Veuillez entre un nombre entre 1 et 100: {Colors.WHITE}"))
            if self.nombre_utilisateur < 1 or self.nombre_utilisateur > 100:
                raise IndexError

        except ValueError:
            print(f"{Colors.RED}Veuillez saisir un nombre!!{Colors.WHITE}")
            return True
        except IndexError:
            print(f"{Colors.YELLOW}ERREUR!! Veuillez écrire un nombre entre 1 et 100....{Colors.WHITE}")
            return True

    def __difference_user_mystere(self):
        """
        Compare la valeur de l'utilisateur et le nombre mystère
        :return:
        Affiche le message approprié pour aiguiller l'utilisateur
        """

        print(f"\nLe nombre mystère est plus grand\n" if self.nombre_mystere > self.nombre_utilisateur else '')
        print(f"\nLe nombre mystère est plus petit\n" if self.nombre_mystere < self.nombre_utilisateur else '')
        self.essais_restants -= 1

    def __str__(self):

        return f'{Colors.GREEN}Bravo, vous avez trouvé le nombre mystère!!{Colors.WHITE}'\
        if self.nombre_mystere == self.nombre_utilisateur else\
            f'{Colors.RED}PERDU, le nombre mystère était {self.nombre_mystere}!!{Colors.WHITE}'


    def game(self):

        while self.essais_restants > 0 and self.nombre_utilisateur != self.nombre_mystere:

            if jeu_mystere.__user_try():
                continue

            jeu_mystere.__difference_user_mystere()

            if self.essais_restants == 0 or self.nombre_mystere == self.nombre_utilisateur:
                print(str(jeu_mystere))
                break


if __name__ == "__main__":
    jeu_mystere = GameMystere()
    jeu_mystere.game()