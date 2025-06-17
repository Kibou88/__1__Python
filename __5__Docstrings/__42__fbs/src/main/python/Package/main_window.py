from PySide6 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    """
    Test de création de fenêtre avec FBS
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application Test")
