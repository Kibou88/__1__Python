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

def screen_grab(coord_table,table):
    """Fonction pour faire une copie d'écran en PNG de l'écran actuel"""
    im = ImageGrab.grab(coord_table) # Créer une copie d'écran et renvoie une image RVB à l'instance im
    im.save(os.getcwd() + '\\s' + str(table) + '.png', 'PNG')
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