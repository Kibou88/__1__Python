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
import tkinter as tk

from map import spain_map
from constantes import DO_VINOS

# Variables de la classe
POS_ROW = 0
WIDTH = 20

window_root = Tk() #Créer l'objet fenêtre racine
window_root.title("VINOS IBERICOS")
window_root.configure(bg="purple")
window_root.geometry('1000x700')

# On définit un premier container à gauche de la fenêtre
left_container = ttk.Frame(window_root, height=680, width=180)
left_container.place(x=25, y=10)

# On positionne un premier label en (10, 10) dans le conteneur de gauche.
first_label = Label(left_container, text="Label 0, 0", fg="white", bg="#FF00FF")
first_label.place(x=0, y=0)

# Puis on positionne un second label en (50, 50) dans le même conteneur.
second_label = Label(left_container, text="Label (50, 50)", fg="white", bg="green")
second_label.place(x=50, y=50)

# On définit un premier container à gauche de la fenêtre
right_container = ttk.Frame(window_root, height=650, width=745, relief='raised', borderwidth=5)
right_container.place(x=230, y=25)

carte = spain_map()
panel = tk.Label(window_root, image = carte)
panel.pack(side = "bottom", fill = "both", expand = "yes")
# On positionne un bouton en (10, 10) dans le conteneur de droite.
# button = Button(right_container, text="Button (10, 10)")
# button.place(x=10, y=10)

window_root.mainloop() #Affiche la fenêtre