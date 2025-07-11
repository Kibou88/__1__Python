import sys
from PySide6 import QtGui
from PySide6.QtGui import QShortcut, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QListWidget, QTextEdit, QGridLayout, QInputDialog, QListWidgetItem
import os

from API.note import get_notes, Note

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setStyleSheet("background-color: rgb(100,100,100);")
        self.setWindowTitle("PyNotes")
        self.setWindowIcon(QIcon("resources/icons/Icon.ico"))
        self.setup_ui()
        self.load_notes()

    def setup_ui(self):
        # L'ORDRE EST IMPORTANT
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.btn_createNote = QPushButton("Create Note")
        self.lw_notes = QListWidget()
        self.te_notes = QTextEdit()

    def modify_widgets(self):
        try:
            current_dir = os.path.dirname(__file__)
            style_path = os.path.join(current_dir, "resources", "style.css")
            with open(style_path, "r") as f:
                self.setStyleSheet(f.read())

        except FileNotFoundError:
            print("No style.css file found")
        except Exception as e:
            print(f"Error: {e}")

    def create_layouts(self):
        self.main_layout = QGridLayout(self)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.btn_createNote, 0, 0, 1, 1)
        self.main_layout.addWidget(self.lw_notes, 1, 0, 1, 1)
        self.main_layout.addWidget(self.te_notes, 0, 1, 2, 1)

    def setup_connections(self):
        """
        Permet de connecter les widgets aux méthodes
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
        Création d'une nouvelle note
        Ouverture d'une boite de dialogue pour le titre. Si un titre a bien été mis, ouverture d'une nouvelle boite
        pour écrire le contenu de la note
        :return:
        """
        # Va permettre d'ouvrir une boite de saisie de texte
        # resultat à True ou False si pas d'erreur lors de la saisie de texte
        note_title, resultat = QInputDialog.getText(self, "Ajouter un titre pour la note", "Titre: ")
        if resultat and note_title:
            note_contents, resultat_contents = QInputDialog.getText(self, "Ajouter un contenu pour la note", "Contenu : ")
            # if resultat_contents and note_contents:
            note_created = Note(title=note_title, contents=note_contents)
            note_created.save()
            self.add_notes_to_listwidgets(note_created)
            # else:
            #     raise Exception("Erreur lors de la creation de la nouvelle note")


    def delete_selected_note(self):
        """
        Suppression de la note sélectionnée
        :return:
        """
        selected_item = self.get_selected_lw_item()
        if selected_item:
            resultat = selected_item.note.delete()
            if resultat:
                self.lw_notes.takeItem(self.lw_notes.row(selected_item))

    def get_selected_lw_item(self):
        selected_items = self.lw_notes.selectedItems()
        if selected_items:
            return selected_items[0]
        return None

    def add_notes_to_listwidgets(self, note):
        lw_item = QListWidgetItem(note.title)
        lw_item.note = note
        self.lw_notes.addItem(lw_item)

    def load_notes(self):
        """
        Chargement des notes depuis le disque
        :return:
        """
        notes_found = get_notes()
        for note in notes_found:
            self.add_notes_to_listwidgets(note)
        print("Chargement des notes depuis le disque")

    def load_note_content(self):
        """
        Chargement du contenu de la note
        :return:
        """
        selected_item = self.get_selected_lw_item()
        if selected_item:
            self.te_notes.setText(selected_item.note.contents)
        else:
            self.te_notes.clear()

    def save_note(self):
        """
        Sauvegarde du contenu de la note
        :return:
        """
        selected_item = self.get_selected_lw_item()
        print(f"{selected_item.note.title}")
        if selected_item:
            selected_item.note.contents = self.te_notes.toPlainText()
            selected_item.note.save()
            print("Note sauvee")

if __name__ == "__main__":
    app = QApplication() # 1. Instantiate QApplication
    windows = MainWindow()
    windows.show()
    exit_code = app.exec() # 2. Invoke app.exec()
    sys.exit(exit_code)