# mouse_event
# But:
# Permet de gérer toutes les actions de la souris
##################################################

# Package pywin32 à installer avant
import win32api, win32con
import time
def left_click_down():
    """Fonction pour appuyer sur le click  gauche
    -------------------------------------
    Fonction win32api.mouse_event(dwFlags, dx, dy, dwdata):
        - dwFlags: Définit l'action de la souris
            * win32con.MOUSEEVENTF_LEFTDOWN
            *win32con.MOUSEEVENTF_LEFTUP
            *win32con.MOUSEEVENTF_MIDDLEDOWN
            *win32con.MOUSEEVENTF_MIDDLEUP
            *win32con.MOUSEEVENTF_LEFTDOWN
    """
    # pos = win32api.GetCursorPos()
    # time.sleep(2)
    # new_pos = (pos[0]-50,pos[1]-50)
    # win32api.SetCursorPos(new_pos)
    # time.sleep(2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) # Le bouton gauche de la souris est appuyé
    time.sleep(1)
#     print("click left down")

def left_click_up():
    """Fonction pour relâcher le click gauche de la souris"""
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) # Le bouton gauche de la souris est relaché
    # time.sleep(1)
    # print("click gauche ok")

def mouse_pos(cord,x_pad,y_pad):
    """Fonction pour déplacer la souris
    -----------------------------------
    Param:
        - cord: Liste qui contient les coordonnées sous la forme cord=(x,y)
        - x_pad: Contient la coordonnée x du coin supérieur gauche
        - y_pad: Contient la coordonnée y du coin supérieur gauche"""
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords(x_pad,y_pad):
    """Fonction pour récupérer l'emplacement de la souris
    -----------------------------------
    Param:
        - x_pad: Contient la coordonnée x du coin supérieur gauche
        - y_pad: Contient la coordonnée y du coin supérieur gauche"""
    x,y=win32api.GetCursorPos()
    # x = x - x_pad
    # y = y - y_pad
    print(x,y)
    return x,y


if __name__ == "__main__":
    left_click_down()