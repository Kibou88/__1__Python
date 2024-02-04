from mouse_event import mouse_pos, left_click_down, left_click_up
import time
from coordonnees import *

def buy_food(food):
    """Fonction du menu du téléphone
    --------------------------------
    Infos:
    -   Positionne la souris sur un des choix du menu du téléphone
    mouse_pos(Cord("phone"))
    mouse_pos(Cord("menu_topping"))
    mouse_pos(Cord("t_shrimp"))
    mouse_pos(Cord("t_nori"))
    mouse_pos(Cord("t_roe"))
    mouse_pos(Cord("t_salmon"))
    mouse_pos(Cord("t_unagi"))
    mouse_pos(Cord("t_exit"))

    mouse_pos(Cord("menu_rice"))
    mouse_pos(Cord("buy_rice"))

    mouse_pos(Cord.delivery_norm)"""
    match food:
        case "nori":
            mouse_pos(Cord("phone"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("menu_topping"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("t_nori"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("delivery_norm"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("t_exit"))

        case "rice":
            mouse_pos(Cord("phone"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("menu_rice"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("buy_rice"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("delivery_norm"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("t_exit"))

        case "roe":
            mouse_pos(Cord("phone"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("menu_topping"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("t_roe"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("delivery_norm"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("t_exit"))


