# notification.py
# ------------------------------------------------------------------
# But:
# Contient l'activation de la notification windows
# ------------------------------------------------------------------
# Date de création: 2025-06-11
# Date de modification: 2025-06-11
# ------------------------------------------------------------------
# Version: V1.0

from sys import platform
from plyer import notification

def send_notification(title_notification, message_notification, app_name):

    if platform == "win32" or platform == "win64":
        icoon = ".\\datas\\icone_server.ico"
        notification.notify(
            title=title_notification,
            message=message_notification,
            app_name=app_name,
            timeout=5,
            app_icon=icoon
        )

if __name__ == "__main__":
    title_notification = "Etat de la demande"
    message_notification = "Demande a valider"
    app_name = "Test"
    send_notification(title_notification, message_notification, app_name)