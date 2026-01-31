# setLevel()
# - Comprendre l'utilisation de setLevel()
# - logger.setLevel(): Définit le niveau minimal que le logger accepte
# - handler.setLevel(): Définit le niveau minimal que le handler traite
###########################################
import logging

#------------- sans setLevel() ------------
logger = logging.getLogger('mon_logger') # Niveau par défaut: WARNING
file_handler = logging.FileHandler('log_notset.txt') # Niveau par défaut: NOTSET

logger.addHandler(file_handler)

logger.debug('debug message') # Ignoré (niveau trop bas)
logger.warning('warning message') # Enregistré (niveau >= WARNING)

#-------------------------------------------------------------------
#------------- avec setLevel() ------------
logger = logging.getLogger('mon_logger2')
logger.setLevel(logging.DEBUG) # Accepte niveau DEBUG et +

# Handler 1: Console (niveau WARNING)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# Handler 2: Fichier (niveau ERROR)
file_handler = logging.FileHandler('log_setlevel.txt')
file_handler.setLevel(logging.ERROR)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug('debug message') # Ignoré par les handlers (niveau trop bas)
logger.warning('warning message') # Affiche en console (niveau >= WARNING)
logger.error('error message') # Affiche partout (console et fichier)
