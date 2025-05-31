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
# Date de modification: 2025-05-30
# ---------------------------------------------------
# Version: V1.0
from PySide6 import QtCore
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton

from boutons import BUTTONS, OPERATIONS


class Calculator(QWidget): #La classe hérite de QWidget
    def __init__(self, nom, width=300, heigth=200):
        super().__init__()
        self.nom = nom
        self.setWindowTitle(nom) #Mettre un nom à la fenêtre
        self.setMinimumSize(width, heigth) # Mets une taille minimale à l'application
        self.resize(width, heigth)  # Fenêtre ajustable en largeur, hauteur

        self.main_layout = QGridLayout(self)

        self.le_result = QLineEdit("0")
        self.le_result.setEnabled(False) # Verrouillage du Line Edit
        self.button = {}

        self.main_layout.addWidget(self.le_result, 0, 0, 1, 4)

        for button_text, button_position in BUTTONS.items():
            button = QPushButton(button_text)
            # *button_position: permet de faire passer toutes les coordonnées du tuple
            # revient à faire button_position[0], ...button_position[3]
            self.main_layout.addWidget(button, *button_position)

            if button_text not in ["=", "C"]:
                button.clicked.connect(self.number_or_operations_pressed)

            self.button[button_text] = button
        self.button["C"].clicked.connect(self.clear_result)
        self.button["="].clicked.connect(self.resultat_operation)
        self.connect_keyboard_shortcut()

    @property
    def result(self):
        """
        Utiliser cette propriété au lieu d'utiliser 'self.result'
        """
        return self.le_result.text()

    def clear_result(self):
        """
        Permet d'effacer toutes les informations du Line Edit
        """
        self.le_result.setText("0")

    def resultat_operation(self):
        """
        Interpètre la chaine de caractère venant du Line Edit en code Python.
        Lève une exception de type SyntaxError et l'affiche sur le Line Edit
        Sinon:
         - Renvoie le calcul en str
        """
        try:
            #eval va permettre d'analyser la chaine de caractère et l'interpréter en code python
            #si eval lit "5 + 10", il comprends : 5 + 10 => 15
            result = eval(self.result.replace("x", "*"))
        except SyntaxError:
            self.le_result.setText("Erreur de syntaxe")

        else:
            self.le_result.setText(str(result))
    def number_or_operations_pressed(self):
        """
        1er bloc if:
            Permet d'éviter des mauvaises erreures de saisies

        2nd bloc if:
            Permet d'afficher la saisie utilisateur en réinitialisation l'affiche si présence du '0'
            ou 'Erreur de syntaxe'
        """
        if self.sender().text() in OPERATIONS:
            if self.result[-1] in OPERATIONS or self.result == '0':
                return


        if self.result == "0" or self.result == "Erreur de syntaxe":
            self.le_result.clear()
        # print(self.sender().text())
        self.le_result.setText(self.result + self.sender().text())

    def connect_keyboard_shortcut(self):
        """
        Gère la gestion des appuis claviers et les connectent aux fonctions adéquates
        """
        for button_text, button in self.button.items():
            QShortcut(QKeySequence(button_text), self, button.clicked.emit)
    # QShortcut(QKeySequence(touche clavier), widget sur lequel l'évènement est déclenché, méthode qui est déclenché
    #                                            self: fenêtre actuelle

        QShortcut(QKeySequence(QtCore.Qt.Key_Space), self, self.resultat_operation)
        QShortcut(QKeySequence(QtCore.Qt.Key_Return), self, self.resultat_operation)
        QShortcut(QKeySequence(QtCore.Qt.Key_Backspace), self, self.delete_last_character)

    def delete_last_character(self):
        """
        Permet de supprimer le dernier caractère ou d'afficher '0' si tous les caractères ont été éffacés
        """
        if len(self.result) > 1:
            self.le_result.setText(self.result[:-1])
        else:
            self.le_result.setText("0")


# -----------------------------------------------------------------------
app = QApplication()

calculatrice = Calculator("Calculatrice")
calculatrice.show()

app.exec() #Lancer l'application