# Exemples de widgets:
# - Apprendre le code pour manipuler:
#   - des boutons
#   - des champs à remplir
#   - du texte
#   - liste
#################################################

from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QListWidget

class PushButton(QPushButton): #Créer un bouton à cliquer
    def __init__(self):
        super().__init__()
        self.setText("Click me")

class LineEdit(QLineEdit): #Créer une boite de texte à écrire
    def __init__(self):
        super().__init__()
        self.setText("A remplir")
        print(self.text())

class Label(QLabel): #Affiche du texte
    def __init__(self):
        super().__init__()
        self.setText("A remplir") #Définir une valeur de la méthode
        print(self.text()) #Accéder à la valeur de la méthode

class ListWidget(QListWidget): #Créer une liste
    def __init__(self):
        super().__init__()
        self.addItem("Item 1")
        self.addItem("Item 2")
        self.addItem("Item 3")

app = QApplication() #1 seule  QApplication

# push_button = PushButton()
# push_button.show()

# line_edit = LineEdit()
# line_edit.show()

# label = Label()
# label.show()

list_widget=ListWidget()
list_widget.show()
app.exec() #Lancer l'application