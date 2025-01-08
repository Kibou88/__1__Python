# Layout
# - Apprendre à utiliser les layouts
####################################
"""
Layout organiser les widgets

QVBoxLayout: Axe Vertical
QHBoxLayout: Axe Horizontal
QStackedLayout
QGridLayout: Grille (ex: pour la calculatrice)
"""

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout ,QGridLayout,QHBoxLayout,QStackedLayout

class MainWindow(QWidget):
    def __init__(self, nom):
        super().__init__()
        self.setWindowTitle(nom) #Mettre un nom à la fenêtre

        main_layout = QVBoxLayout(self) #Le layout DOIT ETRE apparenté à la fenêtre
        for i in range(3):
            button = QPushButton(f"bouton {i}")
            #Ajouter le bouton au layout
            main_layout.addWidget(button)


app = QApplication() #1 seule  QApplication

main_window1 = MainWindow("Fenêtre 1")
main_window1.show()


app.exec() #Lancer l'application