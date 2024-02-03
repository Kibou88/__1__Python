# comparer_images
# But:
# Permet de trouver les différences entre 2 images
##################################################
import cv2
import numpy as np
from QuickGrab import *
from coordonnees import Cord
import os
import time

def compare_picture_all_in_one():
    """Fonction permettant de rassembler toutes les fonctions pour comparer les images"""
    meal_onigiri = 0
    meal_gunkan =0
    meal_caliroll = 0

    for i in range(1,7,1): # Boucle pour prendre en photo les tables
        coord_table = coordonnee_table(i) # Fonction pour récupérer les coordonnées de la bulle à sushi par rapport à la table
        screen_grab(coord_table,i) # Prend le screen de l'endroit et le stocke

    onigiri, caliroll, gunkan = init_images_source()
    s1,s2,s3,s4,s5,s6 = init_images_tables()
    onigiri, caliroll, gunkan, s1,s2,s3,s4,s5,s6 = converter_gray_scale(onigiri, caliroll, gunkan, s1,s2,s3,s4,s5,s6) # Niveau de gris

    # Rassemble les images tables dans une liste et source dans une autre
    origin_sushis = (onigiri, gunkan, caliroll)
    tables = (s1, s2, s3, s4, s5, s6)

    i = 0
    x = 0
    for table in tables:
        i += 1
        recap_error = []
        food = 0
        meal = ""
        for sushi in origin_sushis:
            error, diff = mse(sushi, table)
            recap_error.append((error, food))
            food += 1
        # print("Avant tri: ", recap_error)
        recap_error.sort(key=lambda x: x[0])
        # print("Après tri: ", recap_error)
        if recap_error[0][1] == 0 and recap_error[0][0] <= 10:
            meal = "onigiri"
            meal_onigiri += 1
        elif recap_error[0][1] == 1 and recap_error[0][0] <= 10:
            meal = "gunkan"
            meal_gunkan += 1
        elif recap_error[0][1] == 2 and recap_error[0][0] <= 10:
            meal = "caliroll"
            meal_caliroll += 1
        elif recap_error[0][0] >= 10:
            print(f"Le sushi de la table {i} n'as pas de choix")
            continue
        print(f"Le sushi de la table {i} est {meal}")

    return meal_onigiri, meal_gunkan, meal_caliroll

def init_images_source():
    """Fonction pour récupérer et stocker les images sources
    /!\SOUCI AVEC CE LIEN : \pictures\Images_sources\gunkan.png"
    PASSAGE EN TOUT LOCAL/!\ """

    # Récupérer les images à comparer
    onigiri = cv2.imread("onigiri.png")
    caliroll = cv2.imread("caliroll.png")
    gunkan = cv2.imread("gunkan.png")

    return onigiri, caliroll, gunkan

def init_images_tables():
    """Fonction pour mettre sous cv2 les images des tables"""
    s1 = cv2.imread("s1.png")
    s2 = cv2.imread("s2.png")
    s3 = cv2.imread("s3.png")
    s4 = cv2.imread("s4.png")
    s5 = cv2.imread("s5.png")
    s6 = cv2.imread("s6.png")

    return s1,s2,s3,s4,s5,s6
def converter_gray_scale(onigiri,caliroll, gunkan, s1,s2,s3,s4,s5,s6):
    """Fonction pour convertir en échelle de girs les images"""

    #Convertit les images en échelle de gris
    onigiri = cv2.cvtColor(onigiri,cv2.COLOR_BGR2GRAY)
    gunkan = cv2.cvtColor(gunkan,cv2.COLOR_BGR2GRAY)
    caliroll = cv2.cvtColor(caliroll, cv2.COLOR_BGR2GRAY)
    s1 = cv2.cvtColor(s1, cv2.COLOR_BGR2GRAY)
    s2 = cv2.cvtColor(s2, cv2.COLOR_BGR2GRAY)
    s3 = cv2.cvtColor(s3, cv2.COLOR_BGR2GRAY)
    s4 = cv2.cvtColor(s4, cv2.COLOR_BGR2GRAY)
    s5 = cv2.cvtColor(s5, cv2.COLOR_BGR2GRAY)
    s6 = cv2.cvtColor(s6, cv2.COLOR_BGR2GRAY)

    return onigiri, caliroll, gunkan, s1,s2,s3,s4,s5,s6

    # Définit la fonction pour définir le Mean Squarred Error (Correspondance erreur) entre les images

def mse(sushi, table):
    """Fonction pour comparer les sushis templates avec ce que demande le client"""
    h, w = sushi.shape
    diff = cv2.subtract(sushi, table)
    err = np.sum(diff)
    mse = err / (float(h * w))
    return mse, diff

def coordonnee_table(i):
    """Fonction permettant de renvoyer les coordonnées de l'envie de sushi correspondant au numéro de la table"""
    match i:
        case 1:
            box = (Cord("s1_hg")+ Cord("s1_bd"))
        case 2:
            box = (Cord("s2_hg")+ Cord("s2_bd"))
        case 3:
            box = (Cord("s3_hg")+ Cord("s3_bd"))
        case 4:
            box = (Cord("s4_hg")+ Cord("s4_bd"))
        case 5:
            box = (Cord("s5_hg")+ Cord("s5_bd"))
        case 6:
            box = (Cord("s6_hg")+ Cord("s6_bd"))
    return box

if __name__ == "__main__":
    time.sleep(2)
    # compare_picture_all_in_one()