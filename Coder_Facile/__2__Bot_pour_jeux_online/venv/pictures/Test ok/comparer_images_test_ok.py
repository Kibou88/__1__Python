# comparer_images
# But:
# Permet de trouver les différences entre 2 images
##################################################
import cv2
import numpy as np
import os
import time
from PIL import ImageChops


if __name__ == "__main__":

    # Récupérer les images à comparer
    s1 = cv2.imread("s1.png")
    # cv2.imshow("onigiri", onigiri)
    # cv2.waitKey(2)
    # onigiri2 = cv2.imread("onigiri2.png")
    caliroll = cv2.imread("caliroll.png")
    # caliroll_shape = caliroll.shape

    #Convertit les images en échelle de gris
    s1 = cv2.cvtColor(s1,cv2.COLOR_BGR2GRAY)
    # onigiri2 = cv2.cvtColor(onigiri2,cv2.COLOR_BGR2GRAY)
    caliroll = cv2.cvtColor(caliroll, cv2.COLOR_BGR2GRAY)

    # Définit la fonction pour définir le Mean Squarred Error (Correspondance erreur) entre les images
    def mse(caliroll,s1):
        h, w = caliroll.shape
        diff = cv2.subtract(caliroll,s1)
        err = np.sum(diff**2)
        mse = err/(float(h*w))
        return mse, diff

    error, diff = mse(caliroll,caliroll)
    print("Erreur: ", error) # Renvoie une valeur différente de 0
    cv2.imshow("difference", diff)

    # error, diff2 = mse(onigiri, onigiri2)
    # print("Erreur: ", error)
    # # cv2.imshow("difference", diff2)
    # cv2.waitKey(0)
    # cv2.destroyWindow()
    # if onigiri_shape == caliroll_shape:
    #     print("Ceux sont les mêmes images")
    # else:
    #     print("les images sont différentes")
