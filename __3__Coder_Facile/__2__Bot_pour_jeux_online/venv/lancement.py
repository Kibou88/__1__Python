# lancement.py
# But:
# Permet de cliquer sur tout les boutons jusqu'au démarrage du jeu
############ TEST OK ###########
from mouse_event import *
from coordonnees import *
import time
def lancer_jeu():
    """Fonction pour cliquer sur les boutons pour lancer le jeu"""
    mouse_pos(Cord("play now"))
    left_click_down()
    left_click_up()
    time.sleep(8)

    mouse_pos(Cord("big play"))
    left_click_down()
    left_click_up()
    time.sleep(9)

    mouse_pos(Cord("play"))
    time.sleep(1)
    left_click_down()
    left_click_up()
    time.sleep(1)

    mouse_pos(Cord("skip"))
    time.sleep(1)
    left_click_down()
    left_click_up()
    time.sleep(1)

    mouse_pos(Cord("continue"))
    time.sleep(1)
    left_click_down()
    left_click_up()
    time.sleep(1)

