# logger.py
# --------------------------------
# Purpose:
# Class to configure quickly logger, handler, rotatingFileHandler or timeFileHandler and setLevel
# -------------------------------------
# Creation date: 2026-01-31
# Modification date: 2026-01-31
# ------------------------------------------
# Version V1.0.0

from datetime import datetime
from pathlib import Path
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import logging


class Logs():
    """

    """

    def __init__(self, log_name="logs.log", log_dir="Logs", log_level="DEBUG"):
        if not (log_name.endswith(".log")): # Add '.log' extension if missing
            log_name = log_name + ".log"

        self.log_name = log_name
        self.log_dir = log_dir

        if not (log_level.startswith("logging")): # Add 'logging' at beginning if missing
            log_level = "logging." + log_level
        self.log_level = log_level

        self.logger_name = log_name.split(".")[0] # Bring back the name of the log, will be the name of logger
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(self.log_level) # Configure logger level

        self.current_date = datetime.now().strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
        self.log_file_name = f"{self.current_date}_{self.log_name}" # Log name format "YYYY-MM-DD_logs.log"

        self.time_handler = TimedRotatingFileHandler( # Create a new file log at midnight
            f"{self.log_dir}/{self.logger_name}",
            when="midnight",
        )
        formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
        self.time_handler.setFormatter(formatter)

    def log_debug(self, message):
        







if __name__ == "__main__":
    logger = Logs()