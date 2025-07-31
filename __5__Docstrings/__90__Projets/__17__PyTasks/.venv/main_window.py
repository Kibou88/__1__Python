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
from PySide6 import QtGui, QtCore
from PySide6.QtGui import QShortcut, QIcon, QColor
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QListWidget, QTextEdit, \
    QVBoxLayout, QHBoxLayout, QLineEdit, QInputDialog, QListWidgetItem, QSystemTrayIcon
import os

from resources.constantes import COLORS
from misc.logs import Logs
# from misc.taskitem import TaskItem
import API.task as api

class TaskItem(QListWidgetItem):

    def __init__(self, name, done, list_widget):
        super().__init__(name)
        self.done = done
        self.list_widget = list_widget
        self.name = name

        self.setSizeHint(QSize(self.sizeHint().width(), 100))
        self.list_widget.addItem(self)
        self.set_background_color()

    def toggle_state(self):
        self.done = not self.done
        api.set_tasks_statut(name=self.name, done=self.done)
        self.set_background_color()

    def set_background_color(self):
        colors = COLORS.get(self.done)
        self.setBackground(QColor(*colors)) # * permet d'unpacker le tuple
        color_str = ", ".join(map(str, colors))
        stylesheet = f"""
        QListView::item:selected {{
            background-color: rgb({color_str});
            color: rgb(0, 0, 0);
        }}
        QListView::item:hover {{
            background-color: rgb(220, 220, 220);
        }}
        """
        self.list_widget.setStyleSheet(stylesheet)


class MainWindow(QWidget):
    def __init__(self, log_dir_name="Logs"):
        super().__init__()
        self.logs = Logs(application_name="PyTask", log_dir=log_dir_name)
        self.setWindowTitle("PyPlayer") # Changer le titre

        self.current_dir = os.path.dirname(__file__)
        self.resources_dir = os.path.join(self.current_dir, "resources")

        self.setWindowIcon(QIcon("resources/base/icon.png"))  # Changer le lien
        self.setup_ui()
        self.get_tasks()
        self.center_under_tray()

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
            self.create_tray_icon()
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
        self.lw_tasks = QListWidget()
        self.btn_add = QPushButton()
        self.btn_clean = QPushButton()
        self.btn_quit = QPushButton()

    def modify_widgets(self):
        """
        Show a style for the application
        """
        self.main_layout.setContentsMargins(5, 0, 5, 0)
        self.main_layout.setSpacing(0)

        self.setStyleSheet("border: none;")
        # Qt.FramelessWindowHint: Enlève la barre des menus (réduire, fermer, minimiser)
        # Qt.WindowStaysOnTopHint: Permet de mettre l'appli au 1ere plan
        # | correspond à un "et"
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.btn_add.setIcon(QIcon(os.path.join(self.resources_dir, "base/add.svg")))
        self.btn_clean.setIcon(QIcon(os.path.join(self.resources_dir, "base/clean.svg")))
        self.btn_quit.setIcon(QIcon(os.path.join(self.resources_dir, "base/close.svg")))

        self.btn_add.setFixedSize(45, 45)
        self.btn_clean.setFixedSize(45, 45)
        self.btn_quit.setFixedSize(45, 45)

        self.lw_tasks.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lw_tasks.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def create_tray_icon(self):
        """
        Create the tray icon
        # Icône se trouvant en bas à droite
        """
        self.tray = QSystemTrayIcon()
        icon_path = os.path.join(self.resources_dir, "base/icon.png")
        self.tray.setIcon(QIcon(icon_path))
        self.tray.setVisible(True)

    def create_layouts(self):
        """
        Creation of grid layout
        """
        self.main_layout = QVBoxLayout(self)
        self.layout_buttons = QHBoxLayout()

    def add_widgets_to_layouts(self):
        """
        Add widgets to the layout
        """
        self.main_layout.addWidget(self.lw_tasks)
        self.main_layout.addLayout(self.layout_buttons)

        self.layout_buttons.addWidget(self.btn_add)
        self.layout_buttons.addStretch() # Ajoute un espace afin d'éloigner le bouton "add" et les boutons "clean" et "delete"
        self.layout_buttons.addWidget(self.btn_clean)
        self.layout_buttons.addWidget(self.btn_quit)

    def setup_connections(self):
        """
        Connect widgets to the methods
        """
        self.btn_add.clicked.connect(self.add_task)
        self.btn_clean.clicked.connect(self.clean_task)
        self.btn_quit.clicked.connect(self.close) # Fonction déjà intégré dans le QWidget
        self.lw_tasks.itemClicked.connect(lambda lw_item: lw_item.toggle_state())
        self.tray.activated.connect(self.tray_icon_click)

    def add_task(self):
        task_name, ok = QInputDialog.getText(self, "Ajouter une tâche", "Nom de la tâche:")
        if ok and task_name:
            api.add_tasks(name=task_name)
            self.lw_tasks.addItem(task_name)

    def clean_task(self):
        for i in range(self.lw_tasks.count()):
            lw_item = self.lw_tasks.item(i)
            print(lw_item.done)
            if lw_item.done:
                api.remove_tasks(name=lw_item.name)
            self.get_tasks()
            self.lw_tasks.repaint()

    def get_tasks(self):
        self.lw_tasks.clear()
        tasks = api.get_tasks()
        for task_name, done in tasks.items():
            TaskItem(name=task_name, done=done, list_widget=self.lw_tasks)

    def tray_icon_click(self):
        """
        Hide/show the windows application
        """
        if self.isHidden():
            self.showNormal()
        else:
            self.hide()

    def center_under_tray(self):
        tray_x = self.tray.geometry().x()
        tray_y = self.tray.geometry().y()
        print(tray_x, tray_y)
        w, h = self.sizeHint().toTuple() # Taille de l'appli
        print(w, h)
        self.move(tray_x-w, tray_y-h-100)
if __name__ == "__main__":
    app = QApplication() # 1. Instantiate QApplication
    windows = MainWindow(log_dir_name="Test_log")
    windows.show()
    exit_app_logs = Logs(application_name="PyTask", log_dir="Test_log") # Changer le titre

    exit_code = app.exec() # 2. Invoke app.exec()
    exit_app_logs.log_info("Application is shutting down")
    sys.exit(exit_code)