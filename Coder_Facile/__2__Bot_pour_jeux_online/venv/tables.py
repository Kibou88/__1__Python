from mouse_event import mouse_pos, left_click_down, left_click_up
from coordonnees import *
import time
def clear_tables():
    """Fonction pour nettoyer toutes les tables
    -------------------------------------------
    Infos:
    - Utilise la fonction mouse_pos pour positionner la souris
    - Fonctions left_click_down & left_click_up pour faire un click gauche"""
    # Table 1
    mouse_pos(Cord("table 1"))
    left_click_down()
    left_click_up()

    # Table 2
    mouse_pos(Cord("table 2"))
    left_click_down()
    left_click_up()

    # Table 3
    mouse_pos(Cord("table 3"))
    left_click_down()
    left_click_up()

    # Table 4
    mouse_pos(Cord("table 4"))
    left_click_down()
    left_click_up()

    # Table 5
    mouse_pos(Cord("table 5"))
    left_click_down()
    left_click_up()

    # Table 6
    mouse_pos(Cord("table 6"))
    left_click_down()
    left_click_up()

    time.sleep(1)