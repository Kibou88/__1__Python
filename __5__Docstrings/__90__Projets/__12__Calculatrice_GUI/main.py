# Calculatrice GUI
# ---------------------------------------------------
# But:
# Faire une calculatrice avec une interface graphique
# ---------------------------------------------------
# Critères:
# - Etre auto ajustable
# - Faire toutes les opérations basiques soit au clavier, soit aux touches de la calculatrice
# - Afficher les entrées utilisateurs puis le résultat
# - Pouvoir supprimer si l'entrée utilisateur n'est pas bonne
# ---------------------------------------------------
# Date de création: 2025-05-28
# Date de modification: 2025-05-28
# ---------------------------------------------------
# Version: V1.0


from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
from boutons import BUTTONS
class Calculator(QWidget): #La classe hérite de QWidget
    def __init__(self, nom, width=300, heigth=200):
        super().__init__()
        self.nom = nom
        self.setWindowTitle(nom) #Mettre un nom à la fenêtre
        self.setMinimumSize(width, heigth) # Mets une taille minimale à l'application
        self.resize(width, heigth)  # Fenêtre ajustable en largeur, hauteur

        self.main_layout = QGridLayout(self)
        self.le_result = QLineEdit("0")

        self.button = {}

        self.main_layout.addWidget(self.le_result, 0, 0, 1, 4)

        for button_text, button_position in BUTTONS.items():
            button = QPushButton(button_text)
            # *button_position: permet de faire passer toutes les coordonnées du tuple
            # revient à faire button_position[0], ...button_position[3]
            self.main_layout.addWidget(button, *button_position)
            button.clicked.connect(self.number_or_operations_pressed)
            self.button[button_text] = button

    def number_or_operations_pressed(self):
        print(self.sender().text())
        self.le_result.setText(self.le_result().text() + self.sender().text())




# -----------------------------------------------------------------------
app = QApplication()

calculatrice = Calculator("Calculatrice")
calculatrice.show()

app.exec() #Lancer l'application