# Modules dir et help
# - Apprendre le fonctionnement du module dir
# - Apprendre le fonctionnement du module help
##############################################
import random
from pprint import pprint

print(dir(random)) # Permet d'afficher toutes les fonctions qu'on peut utiliser avec le module
# /!\ TOUT LES NOMS COMMENCANT PAR "_" ou "__" NE DOIVENT PAS ETRE UTILISES
# /!\      CEUX SONT DES FONCTIONS POUR PYTHON /!\

help(random.randint) # Permet l'aide de la fonction utilisée
# Pour quitter, touche 'q' du clavier

pprint(dir(random)) # Améliore l'affichage et la lisibilité. Fonctionne sur des listes, ...