# main.py
# But:
# Contient la logique du code
# -----------------------------------
# Date de création: 2024-09-13
# Date de dernière modification: 2024-09-27
# ------------------------------------------
# version: 4.0
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
# - 1 ligne pour appeler la classe (V5)
# - Création d'une méthode privée __start + passage en méthode statique (V5)
# - NOMBRE_MYSTERE passe en attribut de classe (V5)
# - Simplifications de toutes les méthodes de la classe (V5)
# - Structure du jeu (méthode game) plus efficace (V5)
#-----------------------------------------------------------------------------------

# Appel des modules externes
import random

# Appel des modules internes
from constantes import Colors


class GameMystere:
    """
    Classe contenant les méthodes pour la logique du jeu
    """
    NOMBRE_MYSTERE = random.randint(1, 100)

    def __init__(self):
        print("Bienvenue dans le jeu Le Nombre Mystère\n")
        self. nombre_essais = self.__start()
        self.essais_restants = self.nombre_essais
        self.nombre_utilisateur = 0


    def __str__(self):

        return self.game()


    @staticmethod
    def __start():
        """
        Affiche le message de bienvenue + demande au joueur de saisir le nombre d'essais
        :return:
        (int): nombre essais et nombre essais restants
        """
        return int(input("Veuillez choisir le nombre d'essai maximum: "))

    def __user_try(self):
        """
        Indique au joueur que le nombre d'essais restants, et vérifie la saisie utilisateur
        :return:
        (int): Nombre inscrit par le joueur
        """
        print(f'{Colors.PURPLE}DERNIER ESSAI:' if self.essais_restants == 1 else
              f"\nEssai possible: {self.essais_restants}/{self.nombre_essais}")

        while True:
            choix_utilisateur = input(f"Veuillez entre un nombre entre 1 et 100: {Colors.WHITE}")
            if choix_utilisateur.isdigit() and 1 <= int(choix_utilisateur) <= 100:
                return int(choix_utilisateur)
            print(f"{Colors.YELLOW}ERREUR!! Veuillez écrire un nombre entre 1 et 100....{Colors.WHITE}")

    def __difference_user_mystere(self):
        """
        Compare la valeur de l'utilisateur et le nombre mystère
        :return:
        Affiche le message approprié pour aiguiller l'utilisateur
        """
        return f"\nLe nombre mystère est plus grand\n" if GameMystere.NOMBRE_MYSTERE > self.nombre_utilisateur else \
            f"\nLe nombre mystère est plus petit\n"


    def game(self):
        """
        Contient la structure du jeu
        :return:
        Les phrases si le joueur a gagné ou perdu
        """

        while self.essais_restants > 0 and self.nombre_utilisateur != GameMystere.NOMBRE_MYSTERE:
            self.nombre_utilisateur = self.__user_try()
            self.essais_restants -= 1
            
            if self.nombre_utilisateur == GameMystere.NOMBRE_MYSTERE:
                return f'{Colors.GREEN}Bravo, vous avez trouvé le nombre mystère!!{Colors.WHITE}'
            if self.essais_restants == 0:
                return f'{Colors.RED}PERDU, le nombre mystère était {GameMystere.NOMBRE_MYSTERE}!!{Colors.WHITE}'

            print(self.__difference_user_mystere())



if __name__ == "__main__":
    print(GameMystere())