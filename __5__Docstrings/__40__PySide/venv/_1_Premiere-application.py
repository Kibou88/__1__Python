# Première application en PySide
# - Apprendre à faire une appli et une fenêtre
# Besoin:
# PySide6
################################################
from PySide6.QtWidgets import QApplication, QWidget

class MainWindow(QWidget): #La classe hérite de QWidget
    def __init__(self, nom):
        super().__init__()
        self.nom = nom
        self.setWindowTitle(nom) #Mettre un nom à la fenêtre

app = QApplication() #1 seule  QApplication
"""
Sans passer par la classe
win = QWidget() #Peut avoir plusieurs instances
win.show() #Afficher la fenêtre avec la méthode show
"""
main_window1 = MainWindow("Fenêtre 1")
main_window1.show()

main_window2 = MainWindow("Fenêtre 2")
main_window2.show()

app.exec() #Lancer l'application