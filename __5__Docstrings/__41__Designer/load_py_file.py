# Charger un fichier ui
# ---------------------

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from Form_calculator import Ui_Form

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.ui = Ui_Form Supprimer car MainWindow hérite de Ui_Form
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())