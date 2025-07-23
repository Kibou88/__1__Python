# RotatingFileHandler
# - Apprendre à utiliser RotatingFileHandler
###########################################
import logging
from logging.handlers import RotatingFileHandler

# Création d'un logger nommé
logger = logging.getLogger('mon_logger')
logger.setLevel(logging.DEBUG)  # capturer tous les niveaux >= DEBUG

# Création du RotatingFileHandler :
# - log dans 'app.log'
# - rotation quand le fichier atteint 1 Mo (1_000_000 octets)
# - conserver 3 fichiers de sauvegarde (app.log.1, app.log.2, app.log.3)
rotating_handler = RotatingFileHandler('app.log', maxBytes=1_000_000, backupCount=3)

# Format simple mais informatif
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
rotating_handler.setFormatter(formatter)

# Ajout du handler au logger
logger.addHandler(rotating_handler)

# Exemple de log répétitif pour générer du contenu
for i in range(10000):
    logger.debug(f'Message de debug numéro {i}')
