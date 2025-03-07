# Projet: To Do List
# But:
# Créer une interface pour ajouter/supprimer une tâche à faire (voir __init__ pour plus d'infos)
# ----------------------------------------------------------------------------------------------
# Date de création: 2024-07-09
# Date de modification: 2024-07-11
###################################
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget
from datetime import date, time, datetime

class MainWindow(QWidget):
    def __init__(self, nom):
        self.dt = datetime.now()
        super().__init__()
        self.nom = nom
        self.setWindowTitle(nom)
        self.resize(250,350)
        self.main_layout = QVBoxLayout(self)

        self.lw_todoList = QListWidget()
        self.le_text = QLineEdit(self)
        self.le_text.setPlaceholderText("Tâche à effectuer...") # Permet de mettre un texte en arrière plan
        self.btn_clear = QPushButton("Clear list")


        self.main_layout.addWidget(self.lw_todoList)
        self.main_layout.addWidget(self.le_text)
        self.main_layout.addWidget(self.btn_clear)


        self.le_text.textChanged.connect(self.le_text.setText)
        self.le_text.returnPressed.connect(self.add_text_list) # Ajouter la tâche dans la liste en appuyant sur Entrée
        self.btn_clear.clicked.connect(self.clear_text_list) # Efface toute la liste ainsi que la saisie
        self.lw_todoList.itemDoubleClicked.connect(self.delete_todo)

    def add_text_list(self):
        """
        Si le champ n'est pas vide, on enregistre le texte du champ dans la liste

        :return:
        - Ajoute un élément à la liste
        - Supprime les données du champ
        """
        if self.le_text.text() != "":
            self.lw_todoList.addItem(f"Utilisateur [{dt('%d')}]:")
            self.lw_todoList.addItem(self.le_text.text())
        self.le_text.clear()

    def clear_text_list(self):
        """
        Supprime toutes les données utilisateurs
        :return:
        - N/A
        """
        self.le_text.clear()
        self.lw_todoList.clear()

    def delete_todo(self, item):
        self.lw_todoList.takeItem(self.lw_todoList.row(item))


app = QApplication() #1 seule  QApplication
main_window = MainWindow("To Do List")
main_window.show()

app.exec() #Lancer l'application