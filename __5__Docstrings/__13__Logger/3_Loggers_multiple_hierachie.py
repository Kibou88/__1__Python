# Loggers multiple et hiérachie
# - Apprendre à utiliser les logger multiple
# - Apprendre à utiliser handlers
# - Apprendre à utiliser formatters
###########################################
import logging

# Création et configuration de logger_a
logger_a = logging.getLogger('logger_a')
logger_a.setLevel(logging.DEBUG)  # Logger_a gère tous les niveaux DEBUG et plus

# Handler console pour logger_a (niveau INFO)
console_handler_a = logging.StreamHandler()
console_handler_a.setLevel(logging.INFO)
formatter_a = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler_a.setFormatter(formatter_a)

# Handler fichier pour logger_a (niveau DEBUG)
file_handler_a = logging.FileHandler('log_a.log', mode='w', encoding='utf-8')
file_handler_a.setLevel(logging.DEBUG)
file_handler_a.setFormatter(formatter_a)

# Ajout des handlers à logger_a
logger_a.addHandler(console_handler_a)
logger_a.addHandler(file_handler_a)


# Création et configuration de logger_b
logger_b = logging.getLogger('logger_b')
logger_b.setLevel(logging.WARNING)  # Logger_b gère WARNING et plus

# Handler console pour logger_b (niveau WARNING)
console_handler_b = logging.StreamHandler()
console_handler_b.setLevel(logging.WARNING)
formatter_b = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler_b.setFormatter(formatter_b)

# Handler fichier pour logger_b (niveau ERROR)
file_handler_b = logging.FileHandler('log_b.log', mode='w', encoding='utf-8')
file_handler_b.setLevel(logging.ERROR)
file_handler_b.setFormatter(formatter_b)

# Ajout des handlers à logger_b
logger_b.addHandler(console_handler_b)
logger_b.addHandler(file_handler_b)


# Exemples d'utilisation des loggers

# Logs avec logger_a
logger_a.debug("Message DEBUG venant de logger_a (visible uniquement dans log_a.log)")
logger_a.info("Message INFO venant de logger_a (console et log_a.log)")
logger_a.warning("Message WARNING venant de logger_a (console et log_a.log)")

# Logs avec logger_b
logger_b.info("Message INFO venant de logger_b (n'apparaît pas car niveau WARNING)")  # Ignoré
logger_b.warning("Message WARNING venant de logger_b (console)")
logger_b.error("Message ERROR venant de logger_b (console et log_b.log)")
