# main.py
# ------------
# Purpose:
# Launch the application
# -----------------------
# Creation date: 2025-07-16
# Modification date: 2025-07-16
# --------------------------------
# Version: V1.0.0


import sys
from PySide6.QtWidgets import QApplication
from PySide6 import QtGui
from functools import cached_property

from misc.logs import Logs


if __name__ == "__main__":
    app = QApplication() # 1. Instantiate QApplication
    windows = MainWindow()
    windows.resize(800, 600)
    windows.show()
    exit_app_logs = Logs(application_name="Explorer", log_dir="Logs")

    exit_code = app.exec()  # 2. Invoke app.exec()
    exit_app_logs.log_info("Application is shutting down")
    sys.exit(exit_code)