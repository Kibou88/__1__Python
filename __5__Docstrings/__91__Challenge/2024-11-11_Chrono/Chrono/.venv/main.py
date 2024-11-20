# main.py
# But:
# Contient la logique du code
# -----------------------------------
# Date de création: 2024-11-13
# Date de dernière modification: 2024-11-16
# ------------------------------------------
# version: 1.0

#-----------------------------------------------------------------------------------

# Appel des librairies externes
import time
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
              "Choix 1: Start\n"
              "Choix 2: Afficher le temps\n"
              "Choix 3: Stop\n"
              "Choix 4: Reset\n")
        if keyboard.is_pressed('a'):
            self.start()
            print("Le chrono est lancé\n")

        self.userchoice = int(input("Quel est votre choix? "))

        match self.userchoice:
            case 1:
                self.start()
            case 2:
                self.__repr__()
            case 3:
                self.stop()
            case 4:
                self.reset()


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
    while True:
            my_chrono.hmi()