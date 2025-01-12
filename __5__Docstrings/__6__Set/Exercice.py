"""
Nous avons deux dossiers dans lesquels se trouvent des séquences d'images.
Certaines images sont manquantes.
Le but de l'exercice est de trouver quels images sont manquantes à la fois dans le dossier 1 et le dossier 2.
"""
import os

cur_dir = os.path.dirname(__file__)

dossier_rendu_01 = os.path.join(cur_dir, 'rendus_01')
dossier_rendu_02 = os.path.join(cur_dir, 'rendus_02')

fichiers_01 = os.listdir(dossier_rendu_01)
fichiers_02 = os.listdir(dossier_rendu_02)

resultat = set(fichiers_01) | set(fichiers_02)
all_pictures = set([str(i).zfill(4) + '.jpg' for i in range(1, 101)])
print(sorted(list(all_pictures - resultat)))