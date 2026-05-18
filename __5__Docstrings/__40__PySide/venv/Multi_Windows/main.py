from random import randrange
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget, QApplication

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multi Window")
        self.setFixedSize(600, 400)
        self.layout = QHBoxLayout(self)
        self.btn_new_window = QPushButton("New Window")
        self.windows = {} # Création d'un dico pour stocker les fenêtres ouvertes
        self.btn_new_window.clicked.connect(self.create_new_window)
        self.layout.addWidget(self.btn_new_window)

    def create_new_window(self):
        window_number = randrange(999)
        self.windows[f"Windows {window_number}"] = QWidget()
        self.windows[f"Windows {window_number}"].setWindowTitle(f"Fenêtre {window_number}")
        self.windows[f"Windows {window_number}"].show()

app = QApplication()
win = MainWindow()
win.show()
app.exec()