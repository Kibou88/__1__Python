import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication

from Logs.logs import Logs

if __name__ == "__main__":
    app = QApplication() # 1. Instantiate QApplication
    windows = MainWindow()
    windows.resize(550,600)
    windows.show()
    exit_app_logs = Logs(application_name="PyNotes", log_dir="Logs")

    exit_code = app.exec()  # 2. Invoke app.exec()
    exit_app_logs.log_info("Application is shutting down")
    sys.exit(exit_code)