# Exemples utilisations fonction lambda
######################################

"""
Exemple pour récupérer l'extension des fichiers
"""
import os

fichiers=['/H/Projets/fichier1.py',
          '/H/Projets/fichier2.pptx',
          '/Y/Dossiers/fichier3.txt']

get_fichier= lambda f: os.path.split(f)[-1]
get_ext = lambda f: os.path.splitext(f)[-1]
del_point = lambda f: f.replace('.', '')
process = lambda f: del_point(get_ext(get_fichier(f)))

fichiers_extensions = [os.path.splitext(os.path.split(f)[-1])[-1].replace('.','') for f in fichiers]
fichiers_extensions2 = [process(f) for f in fichiers]
print(fichiers_extensions)
print(fichiers_extensions2)

#############################################################
#############################################################
utilisateurs = [('User1', 'Etienne'),
                ('User4', 'Arnaud'),
                ('User5', 'Camille')]

#Fonction jetable: on ne l'utilise qu'une seule fois
utilisateurs.sort(key=lambda x: x[1]) #Trier la liste par rapport à l'élément 'Arnaud'
print(utilisateurs)