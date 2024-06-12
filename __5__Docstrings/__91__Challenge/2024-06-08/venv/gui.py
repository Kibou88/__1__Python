# gui.py
# But:
# Contient le code pour l'interface graphique
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

# Variables de la classe
POS_ROW = 0
WIDTH = 20

window_root = Tk() #Créer l'objet fenêtre racine
window_root.title("VINOS IBERICOS")
window_root.configure(bg="purple")
window_root.geometry('1000x700')

frm = ttk.Frame(window_root, padding=10) #Créer l'objet cadre dans la fenêtre racine
window_root.columnconfigure(0, weight=1)
window_root.columnconfigure(1, weight=3)
frm.grid() #Créer une grille

ttk.Label(frm, text="Hello World!").grid(column=0, row=0) #Créer un label avec une position dans la grille

# Création d'un bouton pour quitter la fenêtre avec position dans la grille
# ttk.Button(frm, text="Quit", command=window_root.destroy).grid(column=0, row=10)
for i in list(DO_VINOS):
    # Création d'un bouton pour quitter la fenêtre avec position dans la grille
    ttk.Button(frm, text=i, command=window_root.destroy, width=WIDTH).grid(column=0, row=POS_ROW)
    POS_ROW += 1


print(ttk.Button().configure().keys())
print(frm.configure().keys())
style = ttk.Style(window_root)
# print(style.configure().keys())
window_root.mainloop() #Affiche la fenêtre