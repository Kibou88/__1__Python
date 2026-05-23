"""
Page principale + page d'erreur
------------------------------
But:
---
Contient la présentation de la page principale et la page d'erreur
----------------------------------------------------------------------------
Date de création: 2026-01-25
Date de modification: 2026-01-25
----------------------------------------------------------------------------
Version PROTOTYPE:


"""
import time
from pathlib import Path

from tools.class_colors import Colors
from tools.log import Logs

def main_page(log_path) -> str:
    """
    Affiche le menu principale de l'IHM
    :return: user_choice (str): choix utilisateur en lowercase
    """
    log_hmi_path = log_path / "hmi"
    log_hmi = Logs(log_name="HMI", log_path=log_hmi_path)
    while True:
        print(f"{Colors.GREEN}Bienvenue dans le suivi de vos seances de sports\n"
              f"Que voulez-vous faire?{Colors.END}\n"
               f"{Colors.PURPLE}1 - Ajouter une séance{Colors.END}\n"
               f"{Colors.BLUE}2 - Afficher une seance deja effectuee{Colors.END}\n"
               f"{Colors.RED}exit - Quittez le programme{Colors.END}\n")
        user_choice = input("Quel est votre choix? ")

        if user_choice.lower() in ("1", "2", "exit"):
            return user_choice.lower(), log_hmi

        log_hmi.log_warning(f"Choix utilisateur non compris: {user_choice}")
        print("Choix utilisateur non compris")
        time.sleep(1)



def error_page():
    """
    Affiche un message d'erreur suite à le mauvais choix de l'utilisateur
    """
    print(f"{Colors.RED}{Colors.BOLD}Le choix inscrit ne correspond pas a la selection.\n{Colors.END}{Colors.END}")
    time.sleep(1.2)

if __name__ == "__main__":
    LOG_PATH = Path.cwd() / "logs"
    print(main_page(log_path=LOG_PATH))