from mouse_event import mouse_pos, left_click_down, left_click_up
import time
from coordonnees import *
from phone_menu import buy_food
def make_food(food,food_on_hand):
    """Fonction pour créer les sushis
    ---------------------------------
    Infos:
    - Si la valeur 'food' correspond à 1 des recettes indiquées, on fait la recette et on envoie"""
    match food:
        case "caliroll":
            print("California Roll")
            food_on_hand["rice"] -= 1
            food_on_hand["nori"] -= 1
            food_on_hand["roe"] -= 1
            mouse_pos(Cord("f_rice"))
            left_click_down()
            left_click_up()
            time.sleep(0.05)
            mouse_pos(Cord("f_nori"))
            left_click_down()
            left_click_up()
            time.sleep(0.05)
            mouse_pos(Cord("f_roe"))
            left_click_down()
            left_click_up()
            time.sleep(0.1)
            # foldMat()
            # time.sleep(1.5)

        case "onigiri":
            print("Onigiri")
            food_on_hand["rice"] -= 2
            food_on_hand["nori"] -= 1
            mouse_pos(Cord("f_rice"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("f_rice"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            mouse_pos(Cord("f_nori"))
            left_click_down()
            left_click_up()
            time.sleep(0.5)
            # foldMat()
            # time.sleep(1.5)

        case "gunkan":
            print("Gunkan")
            food_on_hand["rice"] -= 1
            food_on_hand["nori"] -= 1
            food_on_hand["roe"] -= 2
            mouse_pos(Cord("f_rice"))
            left_click_down()
            left_click_up()
            time.sleep(0.05)
            mouse_pos(Cord("f_nori"))
            left_click_down()
            left_click_up()
            time.sleep(0.05)
            mouse_pos(Cord("f_roe"))
            left_click_down()
            left_click_up()
            mouse_pos(Cord("f_roe"))
            left_click_down()
            left_click_up()
            time.sleep(0.05)
            # foldMat()
            # time.sleep(1.5)
    return food_on_hand

def foldMat():
    """Fonction pour les coordonnées du tapis à rouler les sushis"""
    mouse_pos(Cord("fold mat"))
    left_click_down()
    left_click_up()
    # time.sleep(1)

def check_food(food_on_hand):
    """Fonction pour vérifier la quantité de nourriture restante"""
    for i,j in food_on_hand.items():
        if i == "nori" or i == "rice" or i == "roe":
            if j <= 4:
                print("%s est bas et a besoin de de remplissage %i")
                buy_food(i)