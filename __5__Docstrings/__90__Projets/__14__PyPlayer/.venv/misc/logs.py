# logs.py
# --------------------------------
# Purpose:
# Permit to save logs for any events of the code
# -------------------------------------
# Creation date: 2025-07-11
# Modification date: 2025-07-11
# ------------------------------------------
# Version V1.0.0

import logging
from datetime import datetime
import os

class Logs():
    """
    This class permit to manage logs file and its level
    """

    def __init__(self, application_name, log_dir="Logs"):
        """
        Intialisation of the logger with the date including in the log_name
        :param application_name: (str) name of the application
        :param log_dir: (str) directory of the log file
        """
        self.application_name = application_name
        self.log_dir = log_dir

        os.makedirs(self.log_dir, exist_ok=True) # Check if "Logs" folder already created

        current_date = datetime.now().strftime("%Y-%m-%d") # Format YYYY-MM-DD
        log_filename = f"{current_date}_{application_name}.log"

        log_path = os.path.join(self.log_dir, log_filename) # Create the path for the log

        logging.basicConfig(level=logging.DEBUG,
                            filename=log_path,
                            filemode='a',
            format=f'%(asctime)s | %(levelname)s | %(message)s')

    def log_debug(self, message):
        """
        Add a log entry for debbugging information (for developpers only)
        NOT FOR PRODUCTION
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | DEBUG | message
        """
        logging.debug(message)

    def log_info(self, message):
        """
        Add a log entry in log for general info
        Examples: user login, file processed, service started
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | INFO | message
        """
        logging.info(message)

    def log_warning(self, message):
        """
        Add a log entry for warning
        Examples: deprecated API usage, recoverable errors, missing optional config
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | WARNING | message
        """
        logging.warning(message)

    def log_error(self, message):
        """
        Add a log entry for errors
        Examples: TypeError, ValueError, ...)
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | ERROR | message
        """
        logging.error(message)

    def log_critical(self, message):
        """
        Add a log entry for critical errors
        Examples: database connection lost, out of memory, security breach
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | CRITICAL | message
        """
        logging.critical(message)

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
