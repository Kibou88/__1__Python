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
from hmi.add_seance import HMI_add_seance


USER_CHOICE = ""
LOG_PATH = Path.cwd() / "logs"
MAIN_LOG = Logs(log_name="Main", log_dir=LOG_PATH)

def programme(USER_CHOICE):

    while USER_CHOICE != "exit":
        USER_CHOICE, log_hmi = main_page(log_dir=LOG_PATH)

        match(USER_CHOICE):
            case "1": # Envoi vers la fonction "Ajout d'une séance"
                warning_add_seance = HMI_add_seance(log=log_hmi)
                if(warning_add_seance):
                    MAIN_LOG.log_warning("Probleme survenu dans la sous-fonction 'Add seance' de l'IHM")

            case "2": # Envoi vers "l'extraction d'une séance"
                pass

            case "erreur":
                error_page()
                MAIN_LOG.log_warning("Problème survenu dans la fonction HMI")

            case "exit":
                MAIN_LOG.log_info("===== Fermeture du programme =====")
                print("Au revoir")

    sys.exit()

if __name__ == "__main__":
    MAIN_LOG.log_info("===== Debut du programme =====")
    programme(USER_CHOICE)