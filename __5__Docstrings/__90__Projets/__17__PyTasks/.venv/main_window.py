# main_window.py
# --------------
# Purpose:
# Create the GUI for PyPlayer
# ---------------------------
# Creation date: 2025-07-13
# Modification date: 2025-07-13
# ------------------------------
# Version V1.0.0:



import sys
from PySide6 import QtGui
from PySide6.QtGui import QShortcut, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QListWidget, QTextEdit, QGridLayout, QInputDialog, QListWidgetItem
import os


from Logs.logs import Logs

class MainWindow(QWidget):
    def __init__(self, log_dir_name="Logs"):
        super().__init__()
        self.logs = Logs(application_name="PyPlayer", log_dir=log_dir_name)
        self.setWindowTitle("PyPlayer") # Changer le titre
        self.setWindowIcon(QIcon("resources/icons/Icon.ico")) # Changer le lien
        self.current_dir = os.path.dirname(__file__)
        self.setup_ui()

    def setup_ui(self):
        """
        Initialize l'UI
        :return:
        Occur an error if the initialization fails
        """
        # L'ORDRE EST IMPORTANT
        try:
            self.create_widgets()
            self.create_layouts()
            self.modify_widgets()
            self.add_widgets_to_layouts()
            self.setup_connections()
        except Exception as e:
            self.logs.log_error(e)
            raise Exception(f"Something went wrong {e}.")
        else:
            self.logs.log_info("Successfully setup UI.")

    def create_widgets(self):
        """
        Create widgets for the application
        """
        pass

    def modify_widgets(self):
        """
        Show a style for the application
        """
        pass

    def create_layouts(self):
        """
        Creation of grid layout
        """
        pass

    def add_widgets_to_layouts(self):
        """
        Add widgets to the layout
        """
        pass

    def setup_connections(self):
        """
        Connect widgets to the methods
        """
        pass



if __name__ == "__main__":
    app = QApplication() # 1. Instantiate QApplication
    windows = MainWindow(log_dir_name="Test_log")
    windows.show()
    exit_app_logs = Logs(application_name="PyPlayer", log_dir="Test_log") # Changer le titre

    exit_code = app.exec() # 2. Invoke app.exec()
    exit_app_logs.log_info("Application is shutting down")
    sys.exit(exit_code)