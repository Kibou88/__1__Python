from mouse_event import mouse_pos, left_click_down, left_click_up
import time
def clear_tables():
    """Fonction pour nettoyer toutes les tables
    -------------------------------------------
    Infos:
    - Utilise la fonction mouse_pos pour positionner la souris
    - Fonctions left_click_down & left_click_up pour faire un click gauche"""
    # Table 1
    mouse_pos((11, 160))
    left_click_down()
    left_click_up()

    # Table 2
    mouse_pos((116, 160))
    left_click_down()
    left_click_up()

    # Table 3
    mouse_pos((216, 160))
    left_click_down()
    left_click_up()

    # Table 4
    mouse_pos((318, 160))
    left_click_down()
    left_click_up()

    # Table 5
    mouse_pos((422, 160))
    left_click_down()
    left_click_up()

    # Table 6
    mouse_pos((527, 160))
    left_click_down()
    left_click_up()

    time.sleep(1)