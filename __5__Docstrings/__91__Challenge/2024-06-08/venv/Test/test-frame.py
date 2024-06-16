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
import os
import tkinter
import tkintermapview
from PIL import Image, ImageTk

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
left_container.configure()
left_container.place(x=25, y=10)

# On positionne un premier label en (10, 10) dans le conteneur de gauche.
first_label = Label(left_container, text="Label 0, 0", fg="white", bg="#FF00FF")
first_label.place(x=0, y=0)

# Puis on positionne un second label en (50, 50) dans le même conteneur.
second_label = Label(left_container, text="Label (50, 50)", fg="white", bg="green")
second_label.place(x=50, y=50)


# create map widget
map_widget = tkintermapview.TkinterMapView(window_root, width=745, height=650, corner_radius=0)
# set current widget position and zoom
map_widget.set_position(40, -3.7) #Centrer sur Madrid
map_widget.set_zoom(7)

current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
blanco = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "images", "blanco.webp")).resize((50, 50)))

marker_1 = map_widget.set_marker(38.3436365, -0.4881708,icon=blanco)  # change position
map_widget.place(x=230, y=25)



window_root.mainloop() #Affiche la fenêtre