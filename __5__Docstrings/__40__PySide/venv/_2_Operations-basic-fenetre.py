# Opérations de base sur la fenêtre
# - Apprendre le code pour manipuler une fenêtre
#################################################

from PySide6.QtWidgets import QApplication, QWidget

class MainWindow(QWidget): #La classe hérite de QWidget
    def __init__(self, nom, largeur=300, hauteur=200):
        super().__init__()
        self.nom = nom
        self.setWindowTitle(nom) #Mettre un nom à la fenêtre
        self.setFixedSize(largeur, hauteur)  # Mettre une taille minimale en largeur x hauteur
        """
        self.setFixedSize(200,240)#Mettre une taille fixe
        self.setMinimumWidth(200) #Mettre une taille minimale sur la largeur
        self.setMinimumHeight(300) #Mettre une taille minimale sur la hauteur
        self.setMinimumSize(200,300) #Mettre une taille minimale en largeur x hauteur
        self.resize(400,400) #Mettre une taille par défaut de la fenêtre. Modifiable
        """

app = QApplication() #1 seule  QApplication

main_window1 = MainWindow("Fenêtre 1", hauteur=300)
main_window1.show()

main_window2 = MainWindow("Fenêtre 2", 480)
main_window2.show()

app.exec() #Lancer l'application