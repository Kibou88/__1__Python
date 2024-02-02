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

def compare_picture_all_in_one(x_pad,y_pad):
    """Fonction permettant de rassembler toutes les fonctions pour comparer les images"""
    onigiri, caliroll, gunkan = ini_images_source()
    for i in range(1,7,1):
        coord_table = coordonnee_table(i,x_pad,y_pad) # Fonction pour récupérer les coordonnées de la bulle à sushi par rapport à la table
        screen_grab(coord_table,i) # Prend le screen de l'endroit et le stocke
        # onigiri, caliroll, gunkan, picture_table = converter_gray_scale(onigiri, caliroll, gunkan, picture_table) # Niveau de gris
        print(f"Table {i} OK")
def ini_images_source():
    """Fonction pour récupérer et stocker les images sources"""

    # Récupérer les images à comparer
    onigiri = cv2.imread("\Pictures\Images_sources\onigiri.png")
    caliroll = cv2.imread("\Pictures\Images_sources\caliroll.png")
    gunkan = cv2.imread("\Pictures\Images_sources\gunkan.png")

    return onigiri, caliroll, gunkan

def converter_gray_scale(onigiri,caliroll, gunkan, picture_table):
    """Fonction pour convertir en échelle de girs les images"""

    #Convertit les images en échelle de gris
    onigiri = cv2.cvtColor(onigiri,cv2.COLOR_BGR2GRAY)
    gunkan = cv2.cvtColor(gunkan,cv2.COLOR_BGR2GRAY)
    caliroll = cv2.cvtColor(caliroll, cv2.COLOR_BGR2GRAY)
    picture_table = cv2.cvtColor(picture_table, cv2.COLOR_BGR2GRAY)

    return onigiri, caliroll, gunkan, picture_table

    # Définit la fonction pour définir le Mean Squarred Error (Correspondance erreur) entre les images
def mse(onigiri,caliroll):
    h, w = onigiri.shape
    diff = cv2.subtract(onigiri,caliroll)
    err = np.sum(diff**2)
    mse = err/(float(h*w))
    return mse, diff

# error, diff = mse(onigiri,caliroll)
# print("Erreur: ", error) # Renvoie une valeur différente de 0
#
# error, diff2 = mse(onigiri, onigiri2)
# print("Erreur: ", error)

def coordonnee_table(i,x_pad,y_pad):
    """Fonction permettant de renvoyer les coordonnées de l'envie de sushi correspondant au numéro de la table"""
    match i:
        case 1:
            # x=Cord("s1_hg")[0]+x_pad
            # y=Cord("s1_hg")[1]+y_pad
            # x1 = Cord("s1_bd")[0] + x_pad
            # y1= Cord("s1_bd")[1] + y_pad
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