# Les signaux
# - Apprendre à utiliser les signaux
####################################
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget): #La classe hérite de QWidget
    def __init__(self, nom):
        super().__init__()
        self.nom = nom
        self.setWindowTitle(nom)
        main_layout = QHBoxLayout(self)

        self.button = QPushButton("Click me")
        button2 = QPushButton("Click me2")
        main_layout.addWidget(self.button)
        main_layout.addWidget(button2)

        # Ne pas mettre les parenthèses pour éviter d'appeler la fonction
        self.button.clicked.connect(self.button_clicked)
        # Envoie True ou False en fonction si le bouton a été cliqué ou pas
        self.button.setCheckable(True)
        button2.pressed.connect(self.button_pressed)
        button2.released.connect(self.button_released)


    def button_clicked(self, check):

        if check:
            self.button.setText("Coché")
        else:
            self.button.setText("Décoché")

    def button_pressed(self):
        print("Le bouton a été pressé")

    def button_released(self):
        print("Le bouton a été relâché")

app = QApplication() #1 seule  QApplication
main_window = MainWindow("Fenêtre 1")
main_window.show()

app.exec() #Lancer l'application
