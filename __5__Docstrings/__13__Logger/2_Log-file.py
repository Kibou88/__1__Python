# Ecrire dans un fichier log
# - Apprendre à écrire dans un fichier log
###########################################
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="Debug.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('La fonction a bien été exécutée')
logging.info("Message d'information général")
logging.warning("Attention!")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")