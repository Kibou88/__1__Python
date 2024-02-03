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
    s2 = cv2.imread("s2.png")
    s3 = cv2.imread("s3.png")
    s4 = cv2.imread("s4.png")
    s5 = cv2.imread("s5.png")
    s6 = cv2.imread("s6.png")
    # cv2.imshow("onigiri", onigiri)
    # cv2.waitKey(2)
    onigiri = cv2.imread("onigiri.png")
    caliroll = cv2.imread("caliroll.png")
    gunkan = cv2.imread("gunkan.png")


    #Convertit les images en échelle de gris
    s1 = cv2.cvtColor(s1,cv2.COLOR_BGR2GRAY)
    s2 = cv2.cvtColor(s2, cv2.COLOR_BGR2GRAY)
    s3 = cv2.cvtColor(s3, cv2.COLOR_BGR2GRAY)
    s4 = cv2.cvtColor(s4, cv2.COLOR_BGR2GRAY)
    s5 = cv2.cvtColor(s5, cv2.COLOR_BGR2GRAY)
    s6 = cv2.cvtColor(s6, cv2.COLOR_BGR2GRAY)
    onigiri = cv2.cvtColor(onigiri,cv2.COLOR_BGR2GRAY)
    caliroll = cv2.cvtColor(caliroll, cv2.COLOR_BGR2GRAY)
    gunkan = cv2.cvtColor(gunkan, cv2.COLOR_BGR2GRAY)

    # Définit la fonction pour définir le Mean Squarred Error (Correspondance erreur) entre les images
    def mse(sushi,table):
        h, w = sushi.shape
        diff = cv2.subtract(sushi,table)
        err = np.sum(diff)
        mse = err/(float(h*w))
        return mse, diff

    origin_sushis = (onigiri, gunkan, caliroll)
    tables = (s1,s2,s3,s4,s5,s6)

    i = 0
    x = 0
    for table in tables:
        i += 1
        recap_error=[]
        food = 0
        meal =""
        for sushi in origin_sushis:

            error, diff = mse(sushi, table)
            recap_error.append((error,food))
            food +=1
        # print("Avant tri: ", recap_error)
        recap_error.sort(key=lambda x: x[0])
        # print("Après tri: ", recap_error)
        if recap_error[0][1] == 0 and recap_error[0][0] <=10:
            meal = "onigiri"
        elif recap_error[0][1] == 1 and recap_error[0][0] <=10:
            meal = "gunkan"
        elif recap_error[0][1] == 2 and recap_error[0][0] <=10:
            meal = "caliroll"
        elif recap_error[0][0] >=10:
            print(f"Le sushi de la table {i} n'as pas de choix")
            continue
        print(f"Le sushi de la table {i} est {meal}")


    # print("Erreur: ", error) # Renvoie une valeur différente de 0
    # cv2.imshow("difference", diff)

    # error, diff2 = mse(onigiri, onigiri2)
    # print("Erreur: ", error)
    # # cv2.imshow("difference", diff2)
    # cv2.waitKey(0)
    # cv2.destroyWindow()
    # if onigiri_shape == caliroll_shape:
    #     print("Ceux sont les mêmes images")
    # else:
    #     print("les images sont différentes")
