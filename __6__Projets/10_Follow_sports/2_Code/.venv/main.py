"""
Main.py
------------------------------
But:
---
Contient la logique principale du programme
----------------------------------------------------------------------------
Date de création: 2026-01-24
Date de modification: 2026-03-27
----------------------------------------------------------------------------
Version PROTOTYPE:


"""
from pathlib import Path
import sys

from tools.log import Logs
from hmi.main_errors_pages import main_page, error_page
from hmi.add_seance import HMI_add_seance
from gestionDB.manage_DataBase import DataBase
from formate_extract_datas import write_report


USER_CHOICE = ""
LOG_DIR = Path.cwd() / "Logs"
MAIN_LOG = Logs(log_name="Main", log_path=LOG_DIR)
DATABASE_NAME = "test"

def programme(USER_CHOICE):

    while USER_CHOICE.lower() != "exit":
        USER_CHOICE = main_page(log_path=LOG_DIR)

        match(USER_CHOICE):
            case "1": # Envoi vers la fonction "Ajout d'une séance"
                # ===== OK ====
                add_seance = HMI_add_seance(log="HMI", log_path=LOG_DIR)
                warning_add_seance, new_seance = add_seance.hmi()
                if(warning_add_seance):
                    MAIN_LOG.log_warning("Probleme survenu dans la sous-fonction 'Add seance' de l'HMI")
                print(new_seance)
                DataBase(dbName="test_user.db", data_to_send=new_seance, log_path=LOG_DIR).process_to_write_data()


            case "2": # Envoi vers "l'extraction d'une séance"
                write_report = write_report(MAIN_LOG)

            case "exit":
                MAIN_LOG.log_info("===== Fermeture du programme =====")
                print("Au revoir")

    sys.exit()

if __name__ == "__main__":
    # print(LOG_DIR)
    MAIN_LOG.log_info("===== Debut du programme =====")
    programme(USER_CHOICE)