# QuickGrab.py
#########################
# Fait avec le magazine Coder facile #3
#########################
#/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\
# Les coordonnées ne sont valables que pour le PC Dell Inspiron 15
#/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\
# Sur un autre PC, les coordonnées x et y sont susceptibles d'être différentes

from PIL import Image, ImageGrab, ImageOps
from numpy import *
import os
import time
from mouse_event import *

# Variables
x_pad = 359  # Coordonnées de x dans le coin supérieur gauche
y_pad = 226  # Coordonnées de y dans le coin supérieur gauche
x_pad2 = 1170 - 359
y_pad2 = 833 - 226
# Dico pour répertorié le nombre d'ingrédients au début du jeu
food_on_hand={
    "shrimp":5,
    "rice":10,
    "nori":10,
    "roe":10,
    "salmon":5,
    "unagi":5
}

def screenGrab():
    """Fonction pour faire une copie d'écran en PNG de l'écran actuel"""

    box = (x_pad+1,y_pad+1,x_pad+x_pad2,y_pad+y_pad2) # Assigne un tuple à la variable "box"
    """ImageGrab.grab prend les paramètres suivants "ImageGrab.grab(x,y,x,y)":
        -   1er x,y => correspond au coin supérieur gauche
        -   2nd x,y => correspond au coin inférieur droit"""
    im = ImageGrab.grab(box) # Créer une copie d'écran et renvoie une image RVB à l'instance im
    print(os.getcwd())
    # im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    """partie "im.save": Appelle la méthode save de la classe Image. Attends 2 paramètres:
                            - Emplacement dans lequel enregistrer le fichier
                            - Format du fichier
        partie "os.getcwd(): Définissons l'emplacement en appelant cette commande => Obtention du répertoire en cours
        partie "\\full__snap" + str(int(time.time()) + '.png': nomme le fichier"""
    return im

def main():
    ingredients = input("Quel est l'ingrédient: ")
    coord_x, coord_y = get_cords(x_pad,y_pad) # Récupère la position de la souris sur x et y
    im = screenGrab() # Fais un screen de l'écran mais sans sauvegarde
    coordinates = coord_x,coord_y
    pixel_rvb = im.getpixel(coordinates) #Récupère la valeur RVB du pixel
    # Inscrit les résultats dans un fichier texte, si il n'existe pas il sera créé
    with open("pixel_ingredients.txt", "a+") as file:
        file.write(f"Les couleurs RVB de {ingredients} sont {pixel_rvb}\t\n")

if __name__ == '__main__':
    time.sleep(1)
    main()