# logger.py
# --------------------------------
# Purpose:
# Class to configure quickly logger, handler, rotatingFileHandler or timeFileHandler and setLevel
# -------------------------------------
# Creation date: 2026-01-31
# Modification date: 2026-02-01
# ------------------------------------------
# Version V1.2
# - Correction problem on create folder parts (V1.1)
# - Ajout d'un handler clear pour éviter les doublons de logs (V1.2)
# - self.configure_setLevel() s'exécute après le self.logger.addHandler (V1.3)
# - Ajout d'une méthode close log pour ferme les logs lors des tests unitaires (V1.3)

from datetime import datetime
from pathlib import Path, WindowsPath
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import logging


class Logs():
    """
    This class permits to manage log files and their levels.
    Every midnight, a new log file is created.
    Log name format: YYYY-MM-DD_log_name.log
    Log level accepted: DEBUG, INFO, WARNING, ERROR, CRITICAL
    Log format: date time | log_name | log_level | log_message
    """

    def __init__(self, log_name="logs.log", log_dir="Logs", log_level="INFO", test = False):
        """
        Initialize the logger, handler and formatter. Create the log_dir folder.
        :param log_name (str): Name of the log file
        :param log_dir (str): Name of the folder where the log file is located.
        :param log_level (str): Level of the log file.
        :param test (bool): If true, close the log file. Defaults to False. (V1.3)
        """
        if not (log_name.endswith(".log")): # Add '.log' extension if missing
            log_name = log_name + ".log"

        self.log_name = log_name
        self.log_dir = log_dir
        self.log_level = log_level
        self.test = test

        # Create the folder if not exist
        if isinstance(log_dir, Path):
            log_dir.mkdir(parents=True, exist_ok=True)
        else:
            # log_dir est une str : on en fait un Path
            Path(log_dir).mkdir(parents=True, exist_ok=True)

        self.init_logger()

        self.current_date = datetime.now().strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
        self.log_file_name = f"{self.current_date}_{self.log_name}" # Log name format "YYYY-MM-DD_logs.log"

        self.init_handler()

        # Supprime handlers existants pour éviter doublons de logs (V1.2)
        if self.logger.handlers:
            for handler in list(self.logger.handlers):
                self.logger.removeHandler(handler)
                handler.close()
        # if self.logger.handlers:
        #     self.logger.handlers.clear()
        self.logger.addHandler(self.time_handler)

        # Must be execute after logger.addHandler (V1.3)
        self.configure_setLevel()  # Configure set level according to log_level wrote

    def init_logger(self):
        """
        Initialize the logger.
        """
        self.logger_name = self.log_name.split(".")[0]  # Bring back the name of the log, will be the name of logger
        self.logger = logging.getLogger(self.logger_name)

    def init_handler(self):
        """
        Initialize the time handler, configure rotate file and formate the log.
        """
        self.time_handler = TimedRotatingFileHandler(  # Create a new file log at midnight
            f"{self.log_dir}/{self.log_file_name}",
            when="midnight"
        )
        formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
        self.time_handler.setFormatter(formatter)

    def configure_setLevel(self):
        """
        Configure the setLevel of logger and handler came from log_level.
        Default, setLevel is in INFO mode.
        """
        match(self.log_level):
            case "DEBUG":
                self.logger.setLevel(logging.DEBUG)
                self.time_handler.setLevel(logging.DEBUG)
            case "INFO":
                self.logger.setLevel(logging.INFO)
                self.time_handler.setLevel(logging.INFO)
            case "WARNING":
                self.logger.setLevel(logging.WARNING)
                self.time_handler.setLevel(logging.WARNING)
            case "ERROR":
                self.logger.setLevel(logging.ERROR)
                self.time_handler.setLevel(logging.ERROR)
            case "CRITICAL":
                self.logger.setLevel(logging.CRITICAL)
                self.time_handler.setLevel(logging.CRITICAL)
            case _:
                print("Set Level choice invalid or empty. Set level is set to INFO")
                self.logger.setLevel(logging.INFO)
                self.time_handler.setLevel(logging.INFO)

    def log_debug(self, message):
        """
        Add a log entry for debbugging information (for developpers only)
        NOT FOR PRODUCTION
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | Application | DEBUG | message
        """
        self.logger.debug(message)

    def log_info(self, message):
        """
        Add a log entry in log for general info
        Examples: user login, file processed, service started
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | Application | INFO | message
        """
        self.logger.info(message)

    def log_warning(self, message):
        """
        Add a log entry for warning
        Examples: deprecated API usage, recoverable errors, missing optional config
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | Application | WARNING | message
        """
        self.logger.warning(message)

    def log_error(self, message):
        """
        Add a log entry for errors
        Examples: TypeError, ValueError, ...)
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | Application | ERROR | message
        """
        self.logger.error(message)

    def log_critical(self, message):
        """
        Add a log entry for critical errors
        Examples: database connection lost, out of memory, security breach
        :param message (str): message to log
        :return: An entry in the log with this format
        2025-07-11 14:36:12,713 | Application | CRITICAL | message
        """
        self.logger.critical(message)

    def close_log(self):
        """
        Use in Test case, to close the log (V1.3)
        :return:
        """
        for handler in list(self.logger.handlers):
            try:
                #
                handler.flush() # Vide et écris le contenu du buffer sur le disque
                handler.close() # Libère le verrou OS sur le fichier → unlink() possible
            except Exception:
                pass
            self.logger.removeHandler(handler)
            # Retirer aussi du registre global de logging
        logging.root.manager.loggerDict.pop(self.logger_name, None)

if __name__ == "__main__":
    try:
        log = Logs(log_name="Test.log", log_dir="Test_Logs", log_level="INFO")
    except:
        print("Probleme dans la creation des logs")
    else:
        log.log_debug("test")
        log.log_info("info")
        log.log_warning("warning")
        log.log_error("error")