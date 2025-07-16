import sys
from PySide6.QtWidgets import QApplication

from main_window import MainWindow
from misc.logs import Logs

if __name__ == "__main__":
    app = QApplication() # 1. Instantiate QApplication
    windows = MainWindow()
    windows.resize(1200,700)
    windows.show()
    exit_app_logs = Logs(application_name="PyExplorer", log_dir="Logs")

    exit_code = app.exec()  # 2. Invoke app.exec()
    exit_app_logs.log_info("Application is shutting down")
    sys.exit(exit_code)