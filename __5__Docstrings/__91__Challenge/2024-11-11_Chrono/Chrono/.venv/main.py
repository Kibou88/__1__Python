# main.py
# But:
# Contient la logique du code
# -----------------------------------
# Date de création: 2024-11-13
# Date de dernière modification: 2024-11-20
# ------------------------------------------
# version: 2.0
# - Ajout de la méthode "keyboard_event" + ajout des touches à utiliser dans l'IHM
# - Arrangement de la logique du code
# - Suppression de la partie "choix utilisateur" de l'IHM
#-----------------------------------------------------------------------------------

# Appel des librairies externes
import time
import os
import keyboard

class Chrono():
    """
    Classe contentant les commandes et l'affichage pour l'appli Chronomètre
    """

    def __init__(self):
        self.starttime = 0
        self.timelaps = 0
        self.timestop = 0
        self.userchoice = 0


    def hmi(self):
        """
        Affiche le menu à l'utilisateur et appelle la méthode par rapport au choix utilisateur
        :return:
        Appel de la méthode correspondant au choix de l'utilisateur
        """
        print("Application Chrono:\n"
              "Choix 1 ou DROITE: Start\n"
              "Choix 2 ou HAUT: Afficher le temps\n"
              "Choix 3 ou GAUCHE: Stop\n"
              "Choix 4 ou BAS: Reset\n"
              "ESPACE: Afficher l'IHM\n")

    def keyboard_event(self):
        """
        Permet de gérer les évènements clavier
        :return:
        Appel de la méthode correspondant en fonction des évènements clavier
        """

        if keyboard.is_pressed('RIGHT'):
            self.start()
            print("Chronomètre lancé")
        elif keyboard.is_pressed('LEFT'):
            self.stop()
            print("Chronomètre arrêté")
        elif keyboard.is_pressed('UP'):
            self.__repr__()
        elif keyboard.is_pressed('DOWN'):
            self.reset()
            print("Reset du chronomètre")
        elif keyboard.is_pressed('SPACE'):
            os.system('cls')
            self.hmi()
        elif keyboard.is_pressed('ESC'):
            print("Fermeture de l'application chronomètre")
            exit()

        time.sleep(0.1)

    def start(self: int) -> float:
        """
        Permet de lancer ou relance le chronomètre
        :return:
        self.timelaps (float) = Valeur de temps en secondes
        """
        self.starttime = time.time()


    def stop(self: float) -> float:
        """
        Permet de faire un stop sur le chronomètre et affiche le temps actuel
        :return:
        TBD (To Be Defined)
        """
        self.timelaps += time.time() - self.starttime
        self.__repr__()

        

    def reset(self: float) -> int:
        """
        Permet de remettre le chronomètre à 0
        :return:
        self.timelaps(int): Remise à 0
        """
        self.timelaps = 0
        self.starttime = 0
        print(f"Chronomètre remis à zéro\n\n")


    def __repr__(self):
        print(f"TimeLaps: {round(self.timelaps, 2)}")


if __name__ == "__main__":
    my_chrono = Chrono()
    my_chrono.hmi()
    while True:
        my_chrono.keyboard_event()

