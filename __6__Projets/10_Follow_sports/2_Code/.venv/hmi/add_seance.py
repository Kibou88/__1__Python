"""
Page ajout séance
------------------------------
But:
---
Contient l'ihm et les saisies utilisateurs pour enregistrées une séance
----------------------------------------------------------------------------
Date de création: 2026-02-01
Date de modification: 2026-03-17
----------------------------------------------------------------------------
Version PROTOTYPE:


"""
from datetime import datetime
from pathlib import Path

from hmi.class_colors import Colors
from tools.log import Logs


class HMI_add_seance():
    """

    """

    def __init__(self, log=None):
        """
        Initialiser les variables de la classe HMI_add_seance.
        :param log (objet log): Enregistre les problèmes de la classe HMI_add_seance sur le log HMI parent
        :parameter warning_to_main (bool): Permet de faire un retour au fichier "main" si un warning a été enregistré
        au cours de l'ajout d'une séance
        :parameter dico_user (dict): Dictionnaire contenant la séance
        """
        self.warning_to_main = False
        self.dico_user = {}
        LOG_PATH = Path.cwd() / "logs" # Création du log dans le répertoire du fichier ==> A modifier plus tard
        self.log = Logs(log_name=log, log_dir=LOG_PATH)
        self.hmi()

    def hmi(self):
        """
        Gestion de l'affichage des messages pour ajouter une séance
        :return:
        """
        print(f"{Colors.LIGHT_PURPLE}==== Ajout d'une seance ====")

        self.ask_check_date()
        self.ask_seance()
        print(self.dico_user)
        return self.warning_to_main

    # ===== OK =====
    def ask_check_date(self):
        """
        Demande la date et vérifie ces conditions:
            - présence de 2 '-' ou 2 '/'
            - contient que des nombres
            - jour compris entre 1 et 31
            - mois compris entre 1 et 12
        :return: self.dico_user (dict): Ajout de la clé [date] avec sa valeur
        """
        while True:

            self.date_seance = input(f"{Colors.LIGHT_PURPLE}Veuillez entrer la date de la seance: ")

            # Check nombre de caractères. Min=8: DD/MM/YY ou Max=10: DD/MM/YYYY
            if not(len(self.date_seance) == 8 or len(self.date_seance) == 10):
                print(f"{Colors.RED}Erreur de syntaxe de la date. Le nombre de caractere pour la date est incoherent "
                  f"avec le format DD/MM/YY ou DD/MM/YYYY")
                self.log.log_warning(f"ADD_SEANCE | Problème nombre de caractere incoherent: {len(self.date_seance)}")
                self.warning_to_main = True
                continue

            # Check présence des bons séparateurs
            if(self.date_seance.count("-") == 2):
                sep = "-"
            elif(self.date_seance.count("/") == 2):
                sep = "/"
            else:
                print(f"{Colors.RED}Erreur de syntaxe de la date. Veuillez mettre 2 '-' ou 2 '/'")
                self.log.log_warning(f"ADD_SEANCE | Problème syntaxe de la date: {self.date_seance}")
                self.warning_to_main = True
                continue

            date_number = self.date_seance.split(sep)

            error_date_flag = False
            # Check si les dates sont bien des nombres et que leurs valeurs sont cohérentes
            for index, i in enumerate(date_number):

                if not i.isdigit():
                    print(f"{Colors.RED}Presence d'un caractere au lieu d'un nombre")
                    error_date_flag = True
                    self.warning_to_main = True
                    self.log.log_error(f"ADD_SEANCE | Problème présence du caractere: {i}")
                    break

                match index:
                    case 0: # Jour compris entre 1 et 31
                        if not (1 <= int(date_number[index]) <= 31):
                            print(f"{Colors.RED}Erreur dans le nombre du jour. Doit etre en 1 et 31")
                            error_date_flag = True
                            self.warning_to_main = True
                            self.log.log_warning(f"ADD_SEANCE | Problème saisie utilisateur pour le jour de la "
                                                 f"séance: {date_number[index]}")

                    case 1: # Mois compris entre 1 et 12
                        if not (1 <= int(date_number[index]) <= 12):
                            print(f"{Colors.RED}Erreur dans le nombre de mois dans l'annee. Doit etre en 1 et 12")
                            error_date_flag = True
                            self.warning_to_main = True
                            self.log.log_warning(f"ADD_SEANCE | Problème saisie utilisateur pour le mois de la "
                                             f"séance: {date_number[index]}")
                if error_date_flag:
                    break

            if error_date_flag:
                continue

            self.dico_user["date"] = self.date_seance
            return

    # ===== OK =====
    def ask_seance(self):
        """
        Menu "ajouter une séance"
        Prends les données utilisateurs et les formattent sous forme de dico
        :return: self.dico_user: (dict):
        """
        exercises = []
        nb_exercices = 0

        print(f"{Colors.END}===========================================")

        # Boucle pour ajouter un nouvel exercice
        while True:

            nb_exercices += 1
            nb_seance = 0
            seance = []

            seance_exercise = {}
            seance_exercise["name"] = input(f"{Colors.LIGHT_PURPLE}Entrer le nom de l'exercice {nb_exercices}: ")

            # Boucle pour ajouter des séances à un exercice
            while True:
                nb_seance += 1
                series_reps_load = {}
                self.error_seance_flag = False

                series_reps_load["series"] = input(f"{Colors.LIGHT_PURPLE}{seance_exercise["name"]} "
                                                       f"seance {nb_seance}: Entrez le nombre de series: ")
                series_reps_load["series"] = self.check_user_input_add_seance(series_reps_load["series"], "int")

                series_reps_load["reps"] = input(f"{Colors.LIGHT_PURPLE}{seance_exercise["name"]} "
                                                     f"seance {nb_seance}: Entrez le nombre de reps: ")
                series_reps_load["reps"] = self.check_user_input_add_seance(series_reps_load["reps"], "int")

                series_reps_load["loads"] = input(f"{Colors.LIGHT_PURPLE}{seance_exercise["name"]} "
                                                  f"seance {nb_seance}: Entrez la charge/poids, en Kg, "
                                                  f"de cette serie: ")
                series_reps_load["loads"] = self.check_user_input_add_seance(series_reps_load["loads"], "int")

                if self.error_seance_flag:
                    print(f"{Colors.RED}Erreur de saisie lors de l'ajout d'une seance. "
                          f"Seance non enregistree{Colors.END}")
                    self.log.log_error(f" ASK SEANCE | Erreur dans l'ajout d'une seance: {series_reps_load}")
                    break

                seance.append(series_reps_load)

                # Choix pour quitter la boucle d'ajout des séances pour un exercice
                continue_add_seance = input(f"{Colors.CYAN}Voulez vous ajouter une autre seance à l'exercice "
                                                 f"{seance_exercise["name"]}? oui ou non:  ")
                if continue_add_seance.lower() not in ["yes", "y", "oui", "o"]:
                    print("Fin ajout seance")
                    break

            seance_exercise["seance"] = seance
            exercises.append(seance_exercise)

            print(f"{Colors.END}===========================================\n")

            # Choix pour quitter la boucle d'ajout des exercices
            continue_add_exercices = input(f"{Colors.CYAN}Voulez vous ajouter une autre exercice? oui ou non:  ")

            if continue_add_exercices.lower() not in ["yes", "y", "oui", "o"]:
                print("Fin ajout exos")
                break

            
        self.dico_user["exercices"] = exercises


    def check_user_input_add_seance(self, variable: str | int, expectedType: str | int) -> int:
        """
        Vérifie si la variable est exclusivement du type prévu. Si ce n'est pas le cas, mets le flag à True
        Exemple:
         - variable: "123", type: "int => OK - error_seance_flag = False => Conversion en int => Retour dans le programme
         - variable: "123g", type: "int => NOK - error_seance_flag = True
        :param variable (str): Variable à tester
        :param expectedType (str ou int): Type attendu de la variable à tester
        :return: self.error_seance_flag (bool): Passe à True si la variable  n'est pas exclusivment du type prévu
        :return: variable (int): Si la variable est comporte uniquement des nombres, alors elle est convertit et retourne
        en int dans le programme
        """

        match(expectedType):
            case "int":
                if not (variable.isdigit()):
                    print(f"{Colors.RED}WARNING!! Veuillez noter UNIQUEMENT des chiffres")
                    self.error_seance_flag = True
                    return variable # Pour que l'erreur soit logguée
                else: # Convertit la variable type 'str' en 'int'
                    return int(variable)

            case "str":
                if not (variable.isalpha()):
                    print(f"{Colors.RED}WARNING!! Veuillez noter UNIQUEMENT des lettres")
                    self.error_seance_flag = True
                    return variable # Pour que l'erreur soit logguée


if __name__ == "__main__":
    test = HMI_add_seance(log="log_hmi")
    print(test.dico_user)