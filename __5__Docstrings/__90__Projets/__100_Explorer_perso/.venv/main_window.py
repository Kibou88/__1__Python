# main_window.py
# --------------
# Purpose:
# Create the GUI for Explorer perso
# ---------------------------
# Creation date: 2025-07-16
# Modification date: 2025-07-17
# ------------------------------
# Version V1.0.0:



import sys
from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtGui import QShortcut, QIcon, QTextCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,  QListWidget, QTextEdit, QHBoxLayout, QInputDialog
from functools import partial
import os
from pathlib import Path

from misc.logs import Logs


class MainWindow(QMainWindow):
    def __init__(self, log_dir_name="Logs"):
        super().__init__()
        self.logs = Logs(application_name="Explorer", log_dir=log_dir_name)
        self.setWindowTitle("Explorer")
        self.setMinimumSize(1200, 700)
        self.logs.log_info("Initializing Explorer")
        icon_path = self.resource_path("resources/icons/icon_app.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.current_dir = os.path.dirname(__file__)
        self.setup_ui()

    def resource_path(self, relative_path):
        """
        Find the good path of file when the code is in developpment or compiled with PyInstaller
        :param relative_path:
        :return:
        """
        # Fonction standard recommandée pour PyInstaller
        # hasattr permet de vérifier si un objet possède un attribut de donnée
        # hasattr(objet, nom_attribut), renvoie True/False en fonction du résultat
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

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
            self.add_actions_to_toolbar()
            self.create_file_model()
            # ----------TO BE DELETED -----------------
            # self.test()
            # ----------------------------------------
        except Exception as e:
            self.logs.log_error(e)
            raise Exception(f"Something went wrong {e}.")
        else:
            self.logs.log_info("Successfully setup UI.")

    def create_widgets(self):
        """
        Create widgets for the application
        """
        self.toolbar = QtWidgets.QToolBar("Toolbar")
        self.toolbar.setIconSize(QtCore.QSize(35,35)) # Taille des icônes
        self.tree_view = QtWidgets.QTreeView()
        self.label_view = QtWidgets.QLabel()
        self.label_view.setText("Sélectionner un fichier")
        self.label_view.setMinimumWidth(int(self.width()/3))

        self.main_widget = QtWidgets.QWidget()

    def modify_widgets(self):
        """
        Show a style for the application
        """
        style_path = os.path.join(self.current_dir, "resources", "style.css")
        try:
            with open(style_path, "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            self.logs.log_error(f"Could not find style.css in {style_path}.")
        except Exception as e:
            self.logs.log_error(e)
        else:
            self.logs.log_info("Successfully applied style.css.")

        self.tree_view.setAlternatingRowColors(True)
        # self.tree_view.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def create_layouts(self):
        """
        Creation of grid layout
        """
        self.main_layout = QtWidgets.QHBoxLayout(self.main_widget)

    def add_widgets_to_layouts(self):
        """
        Add widgets to the layout
        """
        self.addToolBar(QtCore.Qt.TopToolBarArea ,self.toolbar)
        self.setCentralWidget(self.main_widget)
        self.main_layout.addWidget(self.tree_view)
        self.main_layout.addWidget(self.label_view)

    def add_actions_to_toolbar(self):
        """
        Add actions to the toolbar when icon is clicked
        """
        icon_path = os.path.join(self.current_dir, "resources", "svg_files")
        if not icon_path:
            print("svg_files not found")
            self.logs.log_error("Could not find svg_files.")
            self.toolbar.hide()

        locations = ["home", "desktop", "documents", "python", "c"]
        for location in locations:
            icon = os.path.join(icon_path, f"{location}.svg")
            action = self.toolbar.addAction(QtGui.QIcon(icon), location.capitalize())
            action.triggered.connect(partial(self.change_location, location))

    def create_file_model(self):
        """
        Create the structure for the tree view and manage the columns
        """
        self.model = QtWidgets.QFileSystemModel()
        root_path = QtCore.QDir.homePath() # Chemin à la racine
        self.model.setRootPath(root_path) # On se met à la racine
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(root_path))
        self.tree_view.hideColumn(1) # Cache la colonne "Size"
        self.tree_view.hideColumn(2) # Cache la colonne "Type"
        self.tree_view.setColumnWidth(0, self.tree_view.width() - 50)

    def setup_connections(self):
        """
        Connect widgets to the methods
        """
        self.tree_view.clicked.connect(self.treeview_clicked)

    # --------- END of SETUP UI and its methods -------------

    def adjust_labelview_width(self):
        """
        Manage the size of the labelview depends of the windows size
        """
        self.label_view.setMaximumWidth(int(self.width()/2))

    def change_location(self, location):
        """
        Manage the new location when user click on toolbar'shortcut
        :param location: (str) location of folder using in shortcut
        """
        if location == "python":
            python_path = os.path.join(Path.home(), "Desktop", "Code", "__1__Entrainement_Python")
            python_path = os.path.normpath(python_path)
            self.tree_view.setRootIndex(self.model.index(python_path))
        if location == "c":
            c_path = os.path.join(Path.home(), "Desktop", "Code", "__2__C")
            c_path = os.path.normpath(c_path)
            self.tree_view.setRootIndex(self.model.index(c_path))
        if location in ["home", "desktop", "documents"]:
            standard_path = QtCore.QStandardPaths
            print(type(standard_path))
            print(standard_path)
            path = eval(f"standard_path.standardLocations(QtCore.QStandardPaths.{location.capitalize()}Location)")
            print(path)
            self.tree_view.setRootIndex(self.model.index(path[0]))

    def show_contents(self, index):
        """
        Manage the type of visualisation depends if the file is a text or image
        """
        file_path = Path(self.model.filePath(index))
        self.adjust_labelview_width()
        if file_path.suffix.lower() in [".png", ".jpg", ".jpeg"]:
            self.show_image_contents(file_path)
        elif file_path.suffix.lower() in [".txt", ".py"]:
            self.show_text_contents(file_path)
        else:
            self.label_view.setText(f"Ce format {file_path.suffix.lower()} ne peut pas être lu")
            self.logs.log_error(f"Le format {file_path.suffix} du fichier {file_path.name} n'est pas prévu")

    def show_text_contents(self, file_path):
        """
        Show the text contents of the selected file
        :param file_path: (path) Path of the file
        """
        try:
            # Permet de lire l'ensemble du fichier
            with open(file_path, "r", encoding='utf-8') as f:
                self.label_view.setText(f.read())
        except Exception as e:
            self.logs.log_error(e)
        else:
            self.logs.log_info(f"Successfully loaded {file_path.name}")

    def show_image_contents(self, file_path):
        """
        Show the image selected
        :param file_path: (path) Path of the file
        """
        # L'image est chargée dans Pixmap
        image_path = QtGui.QPixmap(file_path)
        # Adapte l'image à la fenêtre de prévisualisation en gardant les proportions
        image_path = image_path.scaled(
            self.label_view.size(),
            aspectMode=QtCore.Qt.KeepAspectRatio,
            mode=QtCore.Qt.SmoothTransformation
            )
        if image_path.isNull():
            self.logs.log_error(f"Impossible de charger l'image {image_path.name}")
            self.label_view.setText(f"Impossible de charger l'image {image_path.name}")
        self.label_view.setPixmap(image_path)

    def treeview_clicked(self, index):
        """
        Method to manage the click on the tree view
        :param index: (QtCore.QModelIndex) receive automatically from clicked.connect
        """
        if not self.model.isDir(index):
            self.show_contents(index)

    # ------- END of application functionalities ---------



if __name__ == "__main__":
    app = QApplication() # 1. Instantiate QApplication
    windows = MainWindow(log_dir_name="Test_log")
    windows.show()
    exit_app_logs = Logs(application_name="Explorer", log_dir="Test_log")

    exit_code = app.exec() # 2. Invoke app.exec()
    exit_app_logs.log_info("Application is shutting down")
    sys.exit(exit_code)