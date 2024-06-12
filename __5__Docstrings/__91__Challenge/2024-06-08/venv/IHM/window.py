# window.py
# But:
# Contient le code pour la fenêtre de l'application
# -----------------------------------
# Date de création: 2024-06-08
# Date de dernière modification: 2024-06-08
# ------------------------------------------
# version: 1.0
# -
#-------------------------------------------
from tkinter import *
from tkinter import ttk

from constantes import DO_VINOS

class MainWindow(Tk):
    """
    Classe MainWindow:
    Permet de définir toutes les caractéristiques de la fenêtre d'application
    Hérite de la classe Tk
    :param
    - Tk: Permet à MainWindow d'hériter de la classe Tk
    """
    # Variables de la classe
    POS_ROW = 15
    POS_COLUMN = 20
    WIDTH = 130
    def __init__(self):
        super().__init__()
        # Windows options
        self.title("VINOS IBEROS")
        self.configure(bg="purple")
        self.geometry('1000x700')

        # Grid options
        frm = ttk.Frame(self, padding=10)  # Créer l'objet cadre dans la fenêtre racine
        # frm.grid()  # Créer une grille
        # ttk.Label(self, text="Hello World!", style='TLabel').grid(column=20, row=0)  # Créer un label avec une position dans la grille

        # Style options
        self.style = ttk.Style(self)
        # Configure le style des labels
        self.style.configure('TLabel', font=('Helvitica', 10), foreground="yellow", background="black")
        # Configure le style des boutons
        self.style.configure(
            'TButton',
            font=('Helvitica', 10),
            borderwidth = '15',
            foreground="#FFCC00", background="#330066",
            padding=5)
        # print(self.style.configure(self).keys())

        # Buttons options
        for i in list(DO_VINOS):
            # Création de tout les boutons pour quitter la fenêtre avec position dans la grille
            button = ttk.Button(self, text=i, command=self.destroy, style='TButton')
            button.place(x=self.POS_COLUMN,y=self.POS_ROW, width=self.WIDTH, height=40)
            self.POS_ROW += 45
            # self.POS_COLUMN += 50
        separator = ttk.Separator(self, orient='vertical')
        separator.pack(fill='y')
        label2 = ttk.Label(self, text="Second Label")
        label2.place(x=100, y =10)
        label2.pack()

if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()  # Affiche la fenêtre