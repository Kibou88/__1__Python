# QuickGrab.py
#########################
# Fait avec le magazine Coder facile #3
# Valable sur le site de jeu:
# https://www.crazygames.com/game/sushi-go-round
#########################
#/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\
# Les coordonnées ne sont valables que pour le PC Dell Inspiron 15
#/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\
# Sur un autre PC, les coordonnées x et y sont susceptibles d'être différentes

from PIL import Image, ImageGrab
import os
import time

def screen_grab():
    """Fonction pour faire une copie d'écran en PNG de l'écran actuel"""
    # Variables
    x_pad = 360  # Coordonnées de x dans le coin supérieur gauche
    y_pad = 227  # Coordonnées de y dans le coin supérieur gauche
    x_pad2 = 1170
    y_pad2 = 834
    box = (x_pad,y_pad,x_pad2,y_pad2) # Assigne un tuple à la variable "box"
    """ImageGrab.grab prend les paramètres suivants "ImageGrab.grab(x,y,x,y)":
        -   1er x,y => correspond au coin supérieur gauche
        -   2nd x,y => correspond au coin inférieur droit"""
    im = ImageGrab.grab(box) # Créer une copie d'écran et renvoie une image RVB à l'instance im
    print(os.getcwd())
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    """partie "im.save": Appelle la méthode save de la classe Image. Attends 2 paramètres:
                            - Emplacement dans lequel enregistrer le fichier
                            - Format du fichier
        partie "os.getcwd(): Définissons l'emplacement en appelant cette commande => Obtention du répertoire en cours
        partie "\\full__snap" + str(int(time.time()) + '.png': nomme le fichier"""

def main():
    screen_grab()

if __name__ == '__main__':
    time.sleep(2)
    main()