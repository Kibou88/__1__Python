# Les signaux
# - Connecter les widgets directement
####################################
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QPushButton, QLabel


class MainWindow(QWidget): #La classe hérite de QWidget
    def __init__(self, nom):
        super().__init__()
        self.nom = nom
        self.setWindowTitle(nom)
        main_layout = QHBoxLayout(self)

        self.le_text = QLineEdit()
        self.lbl_text = QLabel("...")
        self.btn_clear = QPushButton("Clear")

        main_layout.addWidget(self.le_text)
        main_layout.addWidget(self.lbl_text)
        main_layout.addWidget(self.btn_clear)

        self.le_text.textChanged.connect(self.lbl_text.setText) # Copie le label en fct du LineEdit
        self.btn_clear.clicked.connect(self.le_text.clear) # Efface le texte
        # Sinon on peut faire la même chose avec une méthode
        # self.btn_clear.clicked.connect(self.clear_text)

    def clear_text(self):
        self.le_text.clear()
        self.lbl_text.setText("...")


app = QApplication() #1 seule  QApplication
main_window = MainWindow("Fenêtre 1")
main_window.show()

app.exec() #Lancer l'application