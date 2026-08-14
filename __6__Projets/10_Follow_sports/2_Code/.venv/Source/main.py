"""
Main.py
------------------------------
But:
---
Contient la logique principale du programme
----------------------------------------------------------------------------
Date de création: 2026-01-24
Date de modification: 2026-07-15
----------------------------------------------------------------------------
Version V1:


"""
from pathlib import Path
import sys
import os

from tools.class_colors import Colors
from tools.log import Logs
from hmi.main_errors_pages import main_page, error_page
from hmi.add_seance import HMI_add_seance
from hmi.report_seance import ReportSeance
from gestionDB.manage_DataBase import DataBase
from formate_extract_datas.extract_datas import ExtractDatas
from formate_extract_datas.write_report import WriteReport


USER_CHOICE = ""
LOG_DIR = Path.cwd() / "Logs"
MAIN_LOG = Logs(log_name="Main", log_path=LOG_DIR)
DATABASE_NAME = "user"

def programme(USER_CHOICE):

    while USER_CHOICE.lower() != "exit":
        USER_CHOICE = main_page(log_name="HMI", log_path=LOG_DIR)

        match(USER_CHOICE):
            case "1": # Envoi vers la fonction "Ajout d'une séance"
                # ===== OK ====
                add_seance = HMI_add_seance(log_name="HMI", log_path=LOG_DIR)
                warning_add_seance, error_add_seance, new_seance = add_seance.hmi()
                if(warning_add_seance):
                    MAIN_LOG.log_warning("Au moins un probleme survenu dans la sous-fonction 'Add seance' de l'HMI")
                if (error_add_seance):
                    MAIN_LOG.log_error("Au moins une erreur est survenue dans la sous-fonction 'Add seance' de l'HMI")
                # print(new_seance)
                DataBase(dbName=DATABASE_NAME, data_to_send=new_seance,log_name="Gestion_DB", log_path=LOG_DIR).process_to_write_data()


            case "2": # Envoi vers "l'extraction d'une séance"
                # ===== OK ====
                print(f"{Colors.LIGHT_BLUE}")
                dict_extracted, warning_extract, error_extract = \
                    (ExtractDatas(database=DATABASE_NAME, log_name="Formate_Extract_datas", log_path=LOG_DIR)
                     .process_extract_seance())
                print(f"{Colors.YELLOW}")
                if not warning_extract and not error_extract:
                    MAIN_LOG.log_info("Extraction réussi")

                if (warning_extract):
                    MAIN_LOG.log_warning("Un warning est apparu lors de l'extraction des donnees.")
                if (error_extract):
                    MAIN_LOG.log_error("Une erreur est survenue lors de l'extraction des donnees")

                if not error_extract:
                    os.system("cls")

                    ReportSeance(dict_extracted).process_show_seance()
                    print(f"{Colors.END}")
                    os.system("pause")
                    print("\n")

            case "exit":
                MAIN_LOG.log_info("===== Fermeture du programme =====")
                print("Au revoir")

            case _:
                MAIN_LOG.log_warning(f"Saisie utilisateur non valide: {USER_CHOICE}")
                print(f"Saisie utilisateur non valide: {USER_CHOICE}")

    sys.exit()

if __name__ == "__main__":
    MAIN_LOG.log_info("===== Debut du programme =====")
    programme(USER_CHOICE)