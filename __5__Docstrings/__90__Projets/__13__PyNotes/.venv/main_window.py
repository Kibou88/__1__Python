# main_window.py
# --------------
# Purpose:
# Create the GUI for PyNotes
# ---------------------------
# Creation date: 2025-07-11
# Modification date: 2025-07-11
# ------------------------------
# Version V1.1.0:
# - Add logs (V1.1.0)
# - Translate in english (V1.1.0)


import sys
from PySide6 import QtGui
from PySide6.QtGui import QShortcut, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QListWidget, QTextEdit, QGridLayout, QInputDialog, QListWidgetItem
import os

from API.note import get_notes, Note
from Logs.logs import Logs

class MainWindow(QWidget):
    def __init__(self, log_dir_name="Logs"):
        super().__init__()
        self.logs = Logs(application_name="PyNotes", log_dir=log_dir_name)
        self.setWindowTitle("PyNotes")
        self.setWindowIcon(QIcon("resources/icons/Icon.ico"))
        self.setup_ui()
        self.load_notes()

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
        self.btn_createNote = QPushButton("Create Note")
        self.lw_notes = QListWidget()
        self.te_notes = QTextEdit()

    def modify_widgets(self):
        """
        Show a style for the application
        """
        try:
            current_dir = os.path.dirname(__file__)
            style_path = os.path.join(current_dir, "resources", "style.css")
            with open(style_path, "r") as f:
                self.setStyleSheet(f.read())

        except FileNotFoundError:
            self.logs.log_warning(f"Could not find style.css in {style_path}.")
            print("No style.css file found")
        except Exception as e:
            self.logs.log_error(e)
            print(f"Error: {e}")

    def create_layouts(self):
        """
        Creation of grid layout
        """
        self.main_layout = QGridLayout(self)

    def add_widgets_to_layouts(self):
        """
        Add widgets to the layout
        """
        self.main_layout.addWidget(self.btn_createNote, 0, 0, 1, 1)
        self.main_layout.addWidget(self.lw_notes, 1, 0, 1, 1)
        self.main_layout.addWidget(self.te_notes, 0, 1, 2, 1)

    def setup_connections(self):
        """
        Connect widgets to the methods
        """
        self.btn_createNote.clicked.connect(self.create_note)
        self.te_notes.textChanged.connect(self.save_note)
        self.lw_notes.itemSelectionChanged.connect(self.load_note_content)
        # Raccourci clavier de la touche "retour arrière"
        # QtGui.QKeySequence("Backspace") ==> touche "retour arrière"
        # self.lw_notes ==> widget sur lequel le raccourci clavier est activé
        # self.deleted_selected_note ==> méthode à appeler lors de l'appui du raccourci
        QShortcut(QtGui.QKeySequence("Backspace"), self.lw_notes, self.delete_selected_note)
        # Raccourci clavier de la touche "Suppr"
        QShortcut(QtGui.QKeySequence("Delete"), self.lw_notes, self.delete_selected_note)

    def create_note(self):
        """
        Create new note
        Open a dialog box for title and another for contents
        :return:
        Occur an error if the creation fails
        """
        # Va permettre d'ouvrir une boite de saisie de texte
        # resultat à True ou False si pas d'erreur lors de la saisie de texte
        note_title, resultat = QInputDialog.getText(self, "Ajouter un titre pour la note", "Titre: ")
        if resultat and note_title:
            note_contents, resultat_contents = QInputDialog.getText(self, "Ajouter un contenu pour la note", "Contenu : ")
            note_created = Note(title=note_title, contents=note_contents)
            note_created.save()
            self.logs.log_info(f"Note: {note_title} created successfully")
            self.add_notes_to_listwidgets(note_created)
        else:
            self.logs.log_error("An error occur during the creatio of new note.")
            self.logs.log_error(f"Note: {note_title} not created.")
            raise Exception("An error occur during the creatio of new note.")

    def delete_selected_note(self):
        """
        Delete selected note
        """
        selected_item = self.get_selected_lw_item()
        if selected_item:
            resultat = selected_item.note.delete()
            if resultat:
                self.lw_notes.takeItem(self.lw_notes.row(selected_item))
                self.logs.log_info(f"Note: {selected_item.note.title} deleted successfully")

    def get_selected_lw_item(self):
        """
        Return selected note
        """
        selected_items = self.lw_notes.selectedItems()
        if selected_items:
            return selected_items[0]
        return None

    def add_notes_to_listwidgets(self, note):
        """
        Add notes to listwidgets
        :param note:
        """
        lw_item = QListWidgetItem(note.title)
        lw_item.note = note
        self.lw_notes.addItem(lw_item)

    def load_notes(self):
        """
        Load notes from disk
        """
        notes_found = get_notes()
        for note in notes_found:
            self.add_notes_to_listwidgets(note)
        self.logs.log_info(f"Notes loaded: {len(notes_found)}")

    def load_note_content(self):
        """
        Load note contents from the selected note
        """
        selected_item = self.get_selected_lw_item()
        if selected_item:
            self.te_notes.setText(selected_item.note.contents)
            self.logs.log_info(f"Note: {selected_item.note.title}|| contents: {selected_item.note.contents} selected")
        else:
            self.te_notes.clear()

    def save_note(self):
        """
        Save note contents to the selected note
        """
        selected_item = self.get_selected_lw_item()
        if selected_item:
            selected_item.note.contents = self.te_notes.toPlainText()
            selected_item.note.save()

if __name__ == "__main__":
    app = QApplication() # 1. Instantiate QApplication
    windows = MainWindow(log_dir_name="Test_log")
    windows.show()
    exit_app_logs = Logs(application_name="PyNotes", log_dir="Test_log")

    exit_code = app.exec() # 2. Invoke app.exec()
    exit_app_logs.log_info("Application is shutting down")
    sys.exit(exit_code)