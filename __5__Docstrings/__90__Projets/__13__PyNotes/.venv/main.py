import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication() # 1. Instantiate QApplication
    windows = MainWindow()
    windows.resize(550,600)
    windows.show()
    exit_code = app.exec() # 2. Invoke app.exec()
    sys.exit(exit_code)