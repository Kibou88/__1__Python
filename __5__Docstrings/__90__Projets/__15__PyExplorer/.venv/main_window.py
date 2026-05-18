# main_window.py
# --------------
# Purpose:
# Create the GUI for PyExplorer
# ---------------------------
# Creation date: 2025-07-15
# Modification date: 2025-07-15
# ------------------------------
# Version V1.0.0:



import sys
from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtGui import QShortcut, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QListWidget, QTextEdit, QHBoxLayout, \
    QInputDialog, QListWidgetItem, QFileSystemModel
from functools import partial
import os


from misc.logs import Logs

class MainWindow(QMainWindow):
    def __init__(self, log_dir_name="Logs"):
        super().__init__()
        self.logs = Logs(application_name="PyExplorer", log_dir=log_dir_name)
        self.setWindowTitle("PyExplorer")
        self.setWindowIcon(QIcon("resources/icons/Icon.ico"))
        # Variables
        self.current_dir = os.path.dirname(__file__)

        self.setup_ui()
        self.create_file_model()


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
            self.add_actions_to_toolbar()
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
        self.toolbar = QtWidgets.QToolBar("Main ToolBar")
        self.tree_view = QtWidgets.QTreeView()
        self.list_view = QtWidgets.QListView()
        self.slider_iconSize = QtWidgets.QSlider()
        self.main_widget = QtWidgets.QWidget()

    def modify_widgets(self):
        """
        Show a style for the application
        """
        try:
            style_path = os.path.join(self.current_dir, "resources", "style.css")
            with open(style_path, "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            self.logs.log_warning(f"Could not find style.css in {style_path}.")
            print("No style.css file found")
        except Exception as e:
            self.logs.log_error(e)
            print(f"Error: {e}")
        else:
            self.logs.log_info("Successfully load style.css.")
        # mets la liste des dossiers/fichiers d'un dossier en icône
        self.list_view.setViewMode(QtWidgets.QListView.IconMode)
        self.list_view.setUniformItemSizes(True) # Mets les icônes de même taille
        self.list_view.setIconSize(QtCore.QSize(48, 48))

        self.slider_iconSize.setRange(48, 150)
        self.slider_iconSize.setValue(48) # Valeur mini du slider

        # Permet de trier automatiquement par ordre alphabétique les dossiers/fichiers
        # self.tree_view.setSortingEnabled(True)
        self.tree_view.setAlternatingRowColors(True)
        # Permet d'étirer les colonnes du header automatiquement par rapport aux contenus
        self.tree_view.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def create_layouts(self):
        """
        Creation of grid layout
        """
        self.main_layout = QtWidgets.QHBoxLayout(self.main_widget)

    def add_widgets_to_layouts(self):
        """
        Add widgets to the layout
        """
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar) # La barre d'outil est en haut
        self.setCentralWidget(self.main_widget)
        self.main_layout.addWidget(self.tree_view)
        self.main_layout.addWidget(self.list_view)
        self.main_layout.addWidget(self.slider_iconSize)

    def add_actions_to_toolbar(self):
        """
        Add actions to the toolbar
        """
        style_path = os.path.join(self.current_dir, "resources", "base")
        if not style_path:
            self.logs.log_error(f"Could not find base folder in {style_path}.")
            raise FileNotFoundError("Could not find base folder")

        locations = ["home", "desktop", "documents", "movies", "music", "pictures"]
        for location in locations:
            icon = os.path.join(style_path, f"{location}.svg")
            # 2 arguments:
            # - Chemin pour afficher l'icône
            # - Affiche le nom de l'icône si on laisse la souris sur celle-ci (ici "Home", "Desktop", ...)
            action = self.toolbar.addAction(QtGui.QIcon(icon), location.capitalize())
            action.triggered.connect(partial(self.change_location, location))

    def setup_connections(self):
        """
        Connect widgets to the methods
        """
        self.tree_view.clicked.connect(self.treeview_clicked)
        self.list_view.clicked.connect(self.listview_clicked)
        self.list_view.doubleClicked.connect(self.listview_double_clicked)
        self.slider_iconSize.valueChanged.connect(self.change_icon_size)

    def change_icon_size(self, value):
        """
        Change the size of the icon depends of the slider value
        :param value: (int) value of the slider
        """
        self.list_view.setIconSize(QtCore.QSize(value, value))


    def change_location(self, location):
        """
        Change the location when the user clicks on an icon on the toolbar
        """
        standard_path = QtCore.QStandardPaths
        # eval permet d'évaluer comme si c'était une ligne de code
        path = eval(f"standard_path.standardLocations(QtCore.QStandardPaths.{location.capitalize()}Location)")
        self.tree_view.setRootIndex(self.model.index(path[0]))
        self.list_view.setRootIndex(self.model.index(path[0]))

    def create_file_model(self):
        """
        Create the file model depends of the list or tree view
        :return:
        """
        self.model = QtWidgets.QFileSystemModel()
        root_path = QtCore.QDir.homePath() # Chemin à la racine
        self.model.setRootPath(root_path)
        self.tree_view.setModel(self.model)
        self.list_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(root_path))
        self.list_view.setRootIndex(self.model.index(root_path))

    def treeview_clicked(self, index):
        """
        Method to manage the click on the tree view
        :param index: (QtCore.QModelIndex) receive automatically from clicked.connect
        """
        if self.model.isDir(index):
            self.list_view.setRootIndex(index)
        else:
            self.list_view.setRootIndex(index.parent())

    def listview_clicked(self, index):
        """
        Method to manage the click on the list view
        :param index: (QtCore.QModelIndex) receive automatically from clicked.connect
        """
        self.tree_view.selectionModel().setCurrentIndex(index, QtCore.QItemSelectionModel.ClearAndSelect)

    def listview_double_clicked(self, index):
        """
        Method to manage the double click on the list view
        :param index: (QtCore.QModelIndex) receive automatically from clicked.connect
        """
        self.list_view.setRootIndex(index)

if __name__ == "__main__":
    app = QApplication() # 1. Instantiate QApplication
    windows = MainWindow(log_dir_name="Test_log")
    windows.resize(1200, 700)
    windows.show()
    exit_app_logs = Logs(application_name="PyExplorers", log_dir="Test_log")

    exit_code = app.exec() # 2. Invoke app.exec()
    exit_app_logs.log_info("Application is shutting down")
    sys.exit(exit_code)