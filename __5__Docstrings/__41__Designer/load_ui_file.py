# Charger un fichier ui
# ---------------------

import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "Form_calculator.ui"
    ui_file = QFile(ui_file_name)

    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    window.show()

    app.exec()
