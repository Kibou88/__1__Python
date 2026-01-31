# Configuration logs
# - Apprendre différentes configurations pour le log
#  -> répertoire spécifique
#  -> Création d'un nouveau log (ex: chaque log pèsera 5Mo)
#----------------------------------------------------------

from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

# Création du répertoire de log
Path.mkdir(Path.cwd().joinpath('logs'), exist_ok=True)

# Configuration du logger
logger = logging.getLogger("projet")
logger.setLevel(logging.DEBUG)

# Handler rotatif (limite à 1Mo, garde 3 fichiers)
rotating_handler = RotatingFileHandler(
    "logs/projet.log", # Chemin du fichier
    maxBytes = 1 * 1024 * 1024,
    backupCount = 3, # Garde 3 fichiers de sauvegarde
)
rotating_handler.setLevel(logging.DEBUG) # Enregistre tout niveaux de logs

# Formattage des logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rotating_handler.setFormatter(formatter)

# Ajout du handler au logger
logger.addHandler(rotating_handler)

# Test
for i in range(1000000):
    logger.debug('debug message')
    logger.warning('warning message')
    logger.error('error message')