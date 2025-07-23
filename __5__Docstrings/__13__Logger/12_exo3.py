"""
Exercice 3 :
Ajoute à ton logger un FileHandler pour écrire les logs dans un fichier app.log. Teste que
les logs s’affichent toujours en console et s’enregistrent en fichier.
"""
import logging

logger_a = logging.getLogger('logger_a')
logger_a.setLevel(logging.DEBUG)
formatter_a = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler_a = logging.StreamHandler()
console_handler_a.setFormatter(formatter_a)

file_handler_a = logging.FileHandler('app.log')
file_handler_a.setLevel(logging.DEBUG)
file_handler_a.setFormatter(formatter_a)

logger_a.addHandler(console_handler_a)
logger_a.addHandler(file_handler_a)



logger_a.debug('La fonction a bien été exécutée')
logger_a.info("Message d'information général")
logger_a.warning("Attention!")
logger_a.error("Une erreur est arrivée")
logger_a.critical("Erreur critique")