# Module logging
# - Apprendre à les différents niveaux du module logging
# - Configurer le logger
#########################################################

import logging

logging.basicConfig(level=logging.DEBUG) # logging.NIVEAUX
# Prends le NIVEAU + les autres NIVEAUX importants suivants

# Du moins important au plus important
logging.debug('La fonction a bien été exécutée')
logging.info("Message d'information général")
logging.warning("Attention!")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")
