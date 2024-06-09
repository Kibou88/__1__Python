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
    POS_ROW = 0
    POS_COLUMN = 0
    WIDTH = 20
    def __init__(self):
        super().__init__()
        # Windows options
        self.title("VINOS IBEROS")
        self.configure(bg="purple")
        self.geometry('1000x700')

        # Grid options
        frm = ttk.Frame(self, padding=10)  # Créer l'objet cadre dans la fenêtre racine
        frm.grid()  # Créer une grille
        ttk.Label(self, text="Hello World!", style='TLabel').grid(column=20, row=0)  # Créer un label avec une position dans la grille

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
            buttonVin = ttk.Button(self, text=i, command=self.destroy, width=self.WIDTH, style='TButton')
            buttonVin.grid(column=self.POS_COLUMN, row=self.POS_ROW)
            # buttonVin.pack()
            # button.pack()
            self.POS_ROW += 1
            self.POS_COLUMN += 1



if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()  # Affiche la fenêtre