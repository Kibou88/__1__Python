# Logging
# - Création d'un fichier de log très simple
############################################

import logging

logging.basicConfig(filename='test_log.log', level=logging.DEBUG)

def add(a, b):
    logging.info("Exécution de la fonction add")
    logging.debug((a, b))
    if a >0 and b >0:
        logging.debug("A et B sont positifs")
        print(a + b)

add(5, 10)