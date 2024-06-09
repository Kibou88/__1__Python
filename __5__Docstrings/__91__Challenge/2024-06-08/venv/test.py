#---------BIBLIOTHEQUES/MODULES---------
import folium
import webbrowser
from tkinter.messagebox import * # boîte de dialogue
from tkinter import *
import tkinter as tk

#----------FONCTIONS----------
# Fonction carte
def carte():
    # Récupération des données entrées
    nomlieu = nom.get()
    longitude = long.get()
    latitude = lat.get()
    cercle1 = per1.get()
    cercle2 = per2.get()
    # lieu = [46.548312, 3.287667]
    lieu = [longitude, latitude]
    # Création d'une carte
    carte= folium.Map(location=lieu,zoom_start=12)
    # Ajout marqueur avec légende, couleur
    folium.Marker(
        location=lieu,
        popup=nomlieu,
        icon=folium.Icon(color='green')
        ).add_to(carte)
    # Cercle de confinement en mètres (radius = 1000 pour 1 km)
    folium.Circle(lieu,radius = cercle1, fill=True, color='red' ).add_to(carte)
    folium.Circle(lieu,radius = cercle2, fill=True, color='orange' ).add_to(carte)
    # enregistrement et affichage de la carte
    nomcarte = nomlieu+'_'+cercle1+'_'+cercle2+'.html'
    carte.save(nomcarte)
    webbrowser.open(nomcarte)

#----------PROGRAMME PRINCIPAL----------

# Création de la fenêtre principale (main window)
Mafenetre = tk.Tk()
Mafenetre.title('Périmètres')
# Taille de la fenêtre
Mafenetre.geometry("460x220")
Mafenetre.configure(bg = 'orange')
tk.Label(Mafenetre, text = 'Périmètre(s) d'+"'"+'influence ',
bg = 'orange', font=("Arial", 12, "bold")).grid(row=0, column=1)

# widget Nom du Lieu
tk.Label(Mafenetre, text = 'Nom du Lieu ',
bg = 'orange', font=("Arial", 11)).grid(row=1)
nom = tk.Entry(Mafenetre, bg ='bisque', fg='blue', font=("Arial", 11))
nom.grid(row=1, column=1)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=1, column=2)
# widget Longitude
tk.Label(Mafenetre, text = 'Longitude ',
bg = 'orange', font=("Arial", 11)).grid(row=2)
long = tk.Entry(Mafenetre, bg ='bisque', fg='green', font=("Arial", 11))
long.grid(row=2, column=1)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=2, column=2)
# widget Latitude
tk.Label(Mafenetre, text = 'Latitude ',
bg = 'orange', font=("Arial", 11)).grid(row=3)
lat = tk.Entry(Mafenetre, bg ='bisque', fg='green', font=("Arial", 11))
lat.grid(row=3, column=1)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=3, column=2)

# widget Petit périmètre
tk.Label(Mafenetre, text = 'Petit Périmètre (en m) ',
bg = 'orange', font=("Arial", 11)).grid(row=4)
per1 = tk.Entry(Mafenetre, bg ='bisque', fg='red', font=("Arial", 11))
per1.grid(row=4, column=1)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=4, column=2)

# widget Grand périmètre
tk.Label(Mafenetre, text = 'Grand Périmètre (en m) ',
bg = 'orange', font=("Arial", 11)).grid(row=5)
per2 = tk.Entry(Mafenetre, bg ='bisque', fg='red', font=("Arial", 11))
per2.grid(row=5, column=1)
tk.Label(Mafenetre, text = 'Optionnel', bg = 'orange', font=("Arial", 11)).grid(row=5, column=2)

# widget bouton Valider
Valider = tk.Button(Mafenetre, text ='Valider', font=("Arial", 12, "bold"), command=carte)
Valider.grid(row=6, column=1, sticky=tk.W, pady=4)

# widget bouton Quitter
Quitter = tk.Button(Mafenetre, text ='Quitter', font=("Arial", 12, "bold"), command = Mafenetre.destroy)
Quitter.grid(row=6, column=2, sticky=tk.W, pady=4)

# widget Obligatoire
tk.Label(Mafenetre, text = '* Champs obligatoire', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=7, column=1)

Mafenetre.mainloop()