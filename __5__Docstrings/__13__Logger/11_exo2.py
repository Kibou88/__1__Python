"""
Exercice 2 :
Fais un programme avec 2 fichiers modules (module_a.py et module_b.py). Configure un logger nommé pour chaque
module avec un niveau différent (ex: WARNING pour module_a, DEBUG pour module_b) et teste l’émission de
logs de plusieurs niveaux dans chaque.
"""
import logging
logger_a = logging.getLogger('logger_a')
logger_a.setLevel(logging.DEBUG)
console_handler_a = logging.StreamHandler()
formatter_a = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler_a.setFormatter(formatter_a)
logger_a.addHandler(console_handler_a)



logger_a.debug('La fonction a bien été exécutée')
logger_a.info("Message d'information général")
logger_a.warning("Attention!")
logger_a.error("Une erreur est arrivée")
logger_a.critical("Erreur critique")