"""
Main.py
------------------------------
But:
---
Contient la logique principale du programme
----------------------------------------------------------------------------
Date de création: 2026-01-24
Date de modification: 2026-01-24
----------------------------------------------------------------------------
Version PROTOTYPE:


"""
from pathlib import Path
import sys

from tools.log import Logs
from hmi.main_errors_pages import main_page, error_page


USER_CHOICE = ""
LOG_PATH = Path.cwd() / "logs"
MAIN_LOG = Logs(application_name="Application", log_dir=LOG_PATH)

def programme(USER_CHOICE):
    while USER_CHOICE != "exit":

        USER_CHOICE = main_page(LOG_DIR=LOG_PATH)
        match(USER_CHOICE):
            case "1": # Envoi vers la fonction "Ajout d'une séance"
                pass

            case "2": # Envoi vers "l'extraction d'une séance"
                pass

            case "erreur":
                error_page()
                MAIN_LOG.log_warning("Choix utilisateur non compris")

            case "exit":
                MAIN_LOG.log_info("===== Fermeture du programme =====")
                print("Au revoir")

    sys.exit()

if __name__ == "__main__":
    MAIN_LOG.log_info("==============================")
    MAIN_LOG.log_info("===== Debut du programme =====")
    LOG_PATH.mkdir(parents=True, exist_ok=True)
    programme(USER_CHOICE)