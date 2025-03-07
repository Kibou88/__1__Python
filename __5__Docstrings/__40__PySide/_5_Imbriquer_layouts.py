# Imbriquer des Layouts
# - Apprendre à imbriquer des layouts
####################################


from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout ,QGridLayout,QHBoxLayout,QStackedLayout

class MainWindow(QWidget):
    def __init__(self, nom):
        super().__init__()
        self.setWindowTitle(nom)
        # Création des layouts: V=>Vertical // H=>Horizontal
        main_layout = QHBoxLayout(self)  # Le layout DOIT ETRE apparenté à la fenêtre
        left_layout = QVBoxLayout()
        middle_layout = QHBoxLayout()
        right_layout = QVBoxLayout()

        # Ajout des layouts à leur parents
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        # Middle_layout appartient à right_layout
        right_layout.addLayout(middle_layout) #Si on veut mettre ces boutons en bas de la fenêtre déplacé la ligne après la boucle for

        for i in range(11):
            btn = QPushButton(str(i))
            left_layout.addWidget(btn)

        for i in range(11,21):
            btn = QPushButton(str(i))
            right_layout.addWidget(btn)

        for i in range(21,31):
            btn = QPushButton(str(i))
            middle_layout.addWidget(btn)

        # right_layout.addLayout(middle_layout)  # Mets les boutons à la fin de la fenêtre


app = QApplication() #1 seule  QApplication

main_window1 = MainWindow("Fenêtre 1")
main_window1.show()


app.exec() #Lancer l'application