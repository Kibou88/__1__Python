# logs.py
# --------------------------------
# Purpose:
# Permit to save logs for any events of the code
# -------------------------------------
# Creation date: 2025-07-11
# Modification date: 2025-07-22
# ------------------------------------------
# Version V2.0.0
# - Separate Handlers (V2.0.0)
# - Unique logger per instance (V2.0.0)

import logging
from datetime import datetime
import os


class Logs:
    """
    This class permit to manage logs file and its level
    """

    def __init__(self, application_name, log_dir="Logs"):
        """
        Initialisation of the logger with the date including in the log_name
        :param application_name: (str) name of the application
        :param log_dir: (str) directory of the log file
        """
        self.application_name = application_name
        self.log_dir = log_dir

        os.makedirs(self.log_dir, exist_ok=True)

        current_date = datetime.now().strftime("%Y-%m-%d")
        log_filename = f"{current_date}_{application_name}.log"
        self.log_path = os.path.join(self.log_dir, log_filename)

        # Créer un logger spécifique avec un nom unique
        self.logger = logging.getLogger(f"{application_name}_{id(self)}")
        self.logger.setLevel(logging.DEBUG)

        # Éviter la duplication des handlers si le logger existe déjà
        if not self.logger.handlers:
            # Créer un handler pour fichier
            file_handler = logging.FileHandler(self.log_path, mode='a')
            file_handler.setLevel(logging.DEBUG)

            # Créer un formateur
            formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
            file_handler.setFormatter(formatter)

            # Ajouter le handler au logger
            self.logger.addHandler(file_handler)

        # Éviter la propagation vers le logger racine
        self.logger.propagate = False

    def log_debug(self, message):
        """
        Add a log entry for debbugging information (for developpers only)
        NOT FOR PRODUCTION
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | DEBUG | message
        """
        self.logger.debug(message)

    def log_info(self, message):
        """
        Add a log entry in log for general info
        Examples: user login, file processed, service started
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | INFO | message
        """
        self.logger.info(message)

    def log_warning(self, message):
        """
        Add a log entry for warning
        Examples: deprecated API usage, recoverable errors, missing optional config
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | WARNING | message
        """
        self.logger.warning(message)

    def log_error(self, message):
        """
        Add a log entry for errors
        Examples: TypeError, ValueError, ...)
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | ERROR | message
        """
        self.logger.error(message)

    def log_critical(self, message):
        """
        Add a log entry for critical errors
        Examples: database connection lost, out of memory, security breach
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | CRITICAL | message
        """
        self.logger.critical(message)

if __name__ == '__main__':
    try:
        log = Logs(application_name='Test')
    except:
        print("Probleme dans la creation des logs")
    else:
        log.log_debug("test")
        log.log_info("info")
        log.log_warning("warning")
        log.log_error("error")
