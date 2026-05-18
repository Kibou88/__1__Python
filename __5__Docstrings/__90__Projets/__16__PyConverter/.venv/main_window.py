# main_window.py
# --------------
# Purpose:
# Create the GUI for PyConverter
# ---------------------------
# Creation date: 2025-07-20
# Modification date: 2025-07-22
# ------------------------------
# Version V1.0.0:



import sys
import os
from PySide6 import QtGui, QtCore
from PySide6.QtCore import QThread
from PySide6.QtGui import QShortcut, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QListWidget, QTextEdit, QGridLayout, \
    QLabel, QListWidgetItem, QSpinBox, QLineEdit, QMessageBox, QProgressDialog
from functools import cached_property

from thread import Worker
from misc.logs import Logs


class MainWindow(QWidget):

    def __init__(self, log_dir_name="Logs"):
        super().__init__()
        self.log_dir_name = log_dir_name
        self.logs = Logs(application_name="PyConverter", log_dir=self.log_dir_name)
        self.logs.log_info(f"Application PyConverte démarrée")
        self.setWindowTitle("PyConverter")
        self.setWindowIcon(QIcon("resources/Icon.ico"))
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
        self.lbl_quality = QLabel("Qualité:")
        self.spn_quality = QSpinBox()
        self.lbl_size = QLabel("Taille:")
        self.spn_size = QSpinBox()
        self.lbl_output_folder = QLabel("Dossier de sortie:")
        self.le_output_folder = QLineEdit()
        self.lw_files = QListWidget()
        self.btn_convert = QPushButton("Conversion")
        self.lbl_dropInfo = QLabel("^ Déposez les images sur l'interface")

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

        # Alignment
        self.spn_quality.setAlignment(QtCore.Qt.AlignRight)
        self.spn_size.setAlignment(QtCore.Qt.AlignRight)
        self.le_output_folder.setAlignment(QtCore.Qt.AlignRight)

        # Range
        self.spn_quality.setRange(1, 100)
        self.spn_quality.setValue(75)
        self.spn_size.setRange(1, 100)
        self.spn_size.setValue(50)

        # Misc
        self.le_output_folder.setPlaceholderText("Nom du dossier de sortie ...")
        self.le_output_folder.setText("Reduced")
        self.lbl_dropInfo.setVisible(False)

        self.setAcceptDrops(True) # Accepte le Drag and Drop
        self.lw_files.setAlternatingRowColors(True)
        self.lw_files.setSelectionMode(QListWidget.ExtendedSelection) # Sélectionner plusieurs éléments d'un coup

    def create_layouts(self):
        """
        Creation of grid layout
        """
        self.main_layout = QGridLayout(self)

    def add_widgets_to_layouts(self):
        """
        Add widgets to the layout
        """
        self.main_layout.addWidget(self.lbl_quality, 0, 0, 1, 1)
        self.main_layout.addWidget(self.spn_quality, 0, 1, 1, 1)
        self.main_layout.addWidget(self.lbl_size, 1, 0, 1, 1)
        self.main_layout.addWidget(self.spn_size, 1, 1, 1, 1)
        self.main_layout.addWidget(self.lbl_output_folder, 2, 0, 1, 1)
        self.main_layout.addWidget(self.le_output_folder, 2, 1, 1, 1)
        self.main_layout.addWidget(self.lw_files, 3, 0, 1, 2)
        self.main_layout.addWidget(self.lbl_dropInfo, 4, 0, 1, 1)
        self.main_layout.addWidget(self.btn_convert, 5, 0, 1, 2)

    def setup_connections(self):
        """
        Connect widgets to the methods
        """
        QShortcut(QtGui.QKeySequence("Backspace"), self.lw_files, self.delete_selected_items)
        QShortcut(QtGui.QKeySequence("Delete"), self.lw_files, self.delete_selected_items)
        self.btn_convert.clicked.connect(self.convert_images)
        QShortcut(QtGui.QKeySequence("Return"), self.btn_convert, self.convert_images)
        QShortcut(QtGui.QKeySequence("Enter"), self.btn_convert, self.convert_images)
    # ------------- END of setup UI ---------------
    def abort(self):
        """
        Stop the conversion when "Annuler" on QProgressDialog is clicked
        """
        self.worker.runs = False
        self.thread.quit()

    def add_file(self, path):
        """
        Add files to the listwidget
        :param path (str): Path of a file
        """
        # listwidget.count(): Permet de connaitre le nombre d'items présent dans le listwidget

        items = [self.lw_files.item(index).text() for index in range(self.lw_files.count())]
        if path not in items:
            lw_item = QListWidgetItem(path)
            lw_item.setIcon(self.img_unchecked)
            lw_item.processed = False # Stocke le status de la conversion
            self.lw_files.addItem(lw_item)

    def convert_images(self):
        """
        Convert images depends of the quality and size parameters entered
        """
        quality = self.spn_quality.value()
        size = self.spn_size.value() / 100.0 # Avoir un nombre entre 0 et 1
        folder = self.le_output_folder.text()

        lw_items = [self.lw_files.item(index) for index in range(self.lw_files.count())]
        images_to_convert = [1 for lw_item in lw_items if not lw_item.processed]

        if not images_to_convert and not lw_items:
            self.logs.log_warning(f"Aucune image à convertir")
            QMessageBox.warning(self, "Warning", "Aucune image à convertir")
            return False
        elif not images_to_convert and lw_items:
            self.logs.log_info(f"Toutes les images ont déjà été convertit")
            QMessageBox.information(self, "Information", "Toutes les images ont déjà été convertit")
            return False

        self.thread = QThread(self) # Création du thread
        self.worker = Worker(images_to_convert=lw_items,
                             quality=quality,
                             size=size,
                             folder=folder,
                             log_dir=self.log_dir_name)

        self.worker.moveToThread(self.thread) # Va permettre de convertir les images en arrière plan
        self.worker.image_converted.connect(self.image_converted)
        self.thread.started.connect(self.worker.convert_images) # Connecte le start du thread à la méthode convert_images
        self.worker.finished.connect(self.thread.quit) # Connecte le signal finish émis à thread quit
        self.thread.start() # Lance le thread

        # ----------- Progress bar avec fenêtre --------
        # QProgressDialog contient déjà la progress bar
        # QProgressDialog(titre, bouton, départ de la barre, fin de la barre)
        self.prg_dialog = QProgressDialog("Conversion des images", "Annuler", 1, len(images_to_convert))
        self.prg_dialog.canceled.connect(self.abort)
        self.prg_dialog.show()

    def delete_selected_items(self):
        """
        Delete selected items from the listwidget
        """
        for lw_item in self.lw_files.selectedItems():
            row = self.lw_files.row(lw_item)
            try:
                self.lw_files.takeItem(row)
            except Exception as e:
                self.logs.log_error(e)
            else:
                self.logs.log_info(f"Successfully deleted {lw_item.text()}")

    def dragEnterEvent(self, event):
        """
        Show the label "Drop Info" when user enter with its mouse on window application with pictures selected
        :param event (QDragEnterEvent): Event in of drag
        """
        self.lbl_dropInfo.setVisible(True)
        event.accept() # Accepte l'évènement

    def dragLeaveEvent(self, event):
        """
        Hide the label "Drop Info" when user leave with its mouse on window application with pictures selected
        :param event (QDragLeaveEvent): Event out of drag
        """
        self.lbl_dropInfo.setVisible(False)

    def dropEvent(self, event):
        """
        Bring the path of different files drag and drop in the application
        :param event (QDropEvent): Drop event
        """
        event.accept()
        for url in event.mimeData().urls():
            # url.toLocalFile() chemin du fichier
            self.add_file(path=url.toLocalFile())

        self.lbl_dropInfo.setVisible(False)

    def image_converted(self, lw_item, success):
        """
        Manage the state of listWidget about state of success
        :param lw_item (QListWidgetItem): ListWidget item
        :param success (bool): State True/False of converted image
        """
        if success:
            lw_item.setIcon(self.img_checked)
            lw_item.processed = True
            self.prg_dialog.setValue(self.prg_dialog.value() + 1)

    @cached_property
    def img_checked(self):
        return QtGui.QIcon(os.path.join(self.current_dir, "resources", "base", "checked.png"))

    @cached_property
    def img_unchecked(self):
        return QtGui.QIcon(os.path.join(self.current_dir, "resources", "base", "unchecked.png"))


if __name__ == "__main__":
    app = QApplication() # 1. Instantiate QApplication
    windows = MainWindow(log_dir_name="Test_log")
    windows.show()

    exit_app_logs = Logs(application_name="PyConverter", log_dir="Test_log")

    exit_code = app.exec() # 2. Invoke app.exec()
    exit_app_logs.log_info("Application is shutting down")
    sys.exit(exit_code)