# Ecrire dans un fichier log
# - Apprendre à écrire dans un fichier log
# - Apprendre les différents niveaux de log
###########################################
import logging
"""
Utilisation simplifiée avec logging.basicConfig() :
-----------------------------------------------------
level=... : seuil minimal pour enregistrer les messages (ex : logging.INFO).
format=... : chaîne définissant le format affiché (date, niveau, message…).
filename=... et autres options pour fichier, encodage, etc.
"""
logging.basicConfig(level=logging.DEBUG,
                    filename="Debug.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

"""
Les niveaux de log:
-------------------
DEBUG : informations détaillées utiles au débogage.
INFO : informations générales sur le déroulement normal.
WARNING : avertissements sur un problème potentiel.
ERROR : erreurs bloquantes, exceptions.
CRITICAL : erreurs critiques qui nécessitent une action immédiate.
"""
logging.debug('La fonction a bien été exécutée')
logging.info("Message d'information général")
logging.warning("Attention!")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")