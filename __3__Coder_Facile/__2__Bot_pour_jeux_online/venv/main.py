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
import sys
from mouse_event import *
from lancement import lancer_jeu
from comparer_images import compare_picture_all_in_one
from creation_sushi import make_food, check_food, foldMat
from tables import clear_tables

# Variables
x_pad = 360  # Coordonnées de x dans le coin supérieur gauche
y_pad = 227  # Coordonnées de y dans le coin supérieur gauche
x_pad2 = 1170
y_pad2 = 834
# Dico pour répertorié le nombre d'ingrédients au début du jeu
food_on_hand={
    "shrimp":5,
    "rice":10,
    "nori":10,
    "roe":10,
    "salmon":5,
    "unagi":5
}

dico_RVB_food={
    "shrimp":(127, 127, 127),
    "unagi":(204, 172, 89),
    "nori":(255,250,208),
    "fish egg":(34,25,15),
    "salmon":(40,134,210),
    "rice":(255,250,208)
}
def screenGrab():
    """Fonction pour faire une copie d'écran en PNG de l'écran actuel"""

    box = (x_pad,y_pad,x_pad2,y_pad2) # Assigne un tuple à la variable "box"
    """ImageGrab.grab prend les paramètres suivants "ImageGrab.grab(x,y,x,y)":
        -   1er x,y => correspond au coin supérieur gauche
        -   2nd x,y => correspond au coin inférieur droit"""
    im = ImageGrab.grab(box) # Créer une copie d'écran et renvoie une image RVB à l'instance im
    im.save(os.getcwd() + '\\pictures\\Temp\\' + str(box) + '.png', 'PNG')
    """partie "im.save": Appelle la méthode save de la classe Image. Attends 2 paramètres:
                            - Emplacement dans lequel enregistrer le fichier
                            - Format du fichier
        partie "os.getcwd(): Définissons l'emplacement en appelant cette commande => Obtention du répertoire en cours
        partie "\\full__snap" + str(int(time.time()) + '.png': nomme le fichier"""
    # return im

def main():
    name_button = input("Nom du ingrédient: ")
    coord_x, coord_y = get_cords(x_pad,y_pad) # Récupère la position de la souris sur x et y
    im = screenGrab() # Fais un screen de l'écran mais sans sauvegarde
    coordinates = coord_x,coord_y
    pixel_rvb = im.getpixel(coordinates) #Récupère la valeur RVB du pixel
    # Inscrit les résultats dans un fichier texte, si il n'existe pas il sera créé
    with open("pixel_ingredients.txt", "a+") as file:
        file.write(f"Les RVB de {name_button} sont {pixel_rvb}\t\n")
        file.write(f"{type(im)}")

if __name__ == '__main__':
    lancer_jeu()
    while True:
        # main()
        # time.sleep(2)
        meal_onigiri, meal_gunkan, meal_caliroll = compare_picture_all_in_one()

        check_food(food_on_hand)
        for onigiri in range(meal_onigiri):
            food_on_hand = make_food("onigiri", food_on_hand)
            foldMat()
            print(f"Onigiri envoyé")
            check_food(food_on_hand)

        for gunkan in range(meal_gunkan):
            food_on_hand = make_food("gunkan", food_on_hand)
            foldMat()
            print(f"Gunkan envoyé")
            check_food(food_on_hand)
        for caliroll in range(meal_caliroll):
            food_on_hand = make_food("caliroll", food_on_hand)
            foldMat()
            print(f"Caliroll envoyé")
            check_food(food_on_hand)
        time.sleep(1)
        clear_tables()
        print("\n")