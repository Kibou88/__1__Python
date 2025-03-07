# Informations Partial
# - Envoyer des informations avec Partial
####################################
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QPushButton, QLabel
from functools import partial

class MainWindow(QWidget): #La classe hérite de QWidget
    def __init__(self, nom):
        super().__init__()
        self.nom = nom
        self.setWindowTitle(nom)
        main_layout = QHBoxLayout(self)

        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")

        main_layout.addWidget(self.btn_left)
        main_layout.addWidget(self.btn_right)

        # D'abord mettre la méthode a appelé puis les arguments à passer
        self.btn_left.clicked.connect(partial(self.button_clicked, "Bouton de gauche"))
        self.btn_right.clicked.connect(partial(self.button_clicked, "Bouton de droite"))


    def button_clicked(self, message):
        print(message)



app = QApplication() #1 seule  QApplication
main_window = MainWindow("Fenêtre 1")
main_window.show()

app.exec() #Lancer l'application