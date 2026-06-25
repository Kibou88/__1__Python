"""
Page ajout séance
------------------------------
But:
---
Contient l'ihm et les saisies utilisateurs pour enregistrées une séance
----------------------------------------------------------------------------
Date de création: 2026-02-01
Date de modification: 2026-03-28
----------------------------------------------------------------------------
Version PROTOTYPE:


"""
from datetime import datetime
from pathlib import Path

from tools.class_colors import Colors
from tools.log import Logs


class HMI_add_seance():
    """
    Gère l'interface de saisie pour l'ajout d'une séance.

    Cette classe collecte les informations saisies par l'utilisateur
    (date, exercices, séries, répétitions et charge), vérifie leur cohérence
    et renvoie un dictionnaire prêt à être exploité par le reste du programme.

    Attributes:
        warning_to_main (bool): Indique si une anomalie a été détectée pendant la saisie.
        dico_user (dict): Dictionnaire contenant la séance saisie par l'utilisateur.
        log (Logs): Instance utilisée pour enregistrer les erreurs et avertissements.
    """

    def __init__(self, log_name="HMI_add_seance", log_path=Path.cwd()/ "Test_log"):
        """
        Initialise l'interface de saisie et le système de log.

        Args:
            log_name (str, optional): Nom utilisé pour le fichier de log.
                Defaults to "HMI_add_seance".
            log_path (Path, optional): Dossier de stockage des logs.
                Defaults to Path.cwd() / "Test_log".
        """
        self.warning_to_main = False
        self.dico_user = {}
        self.log = Logs(log_name=log_name, log_path=log_path)

    def hmi(self) -> (bool | dict):
        """
        Lance le flux complet de saisie d'une séance.

        La méthode demande d'abord la date, puis les exercices et leurs séries.
        Elle renvoie un indicateur d'avertissement ainsi que les données saisies.

        Returns:
            bool | dict: Tuple contenant le flag d'avertissement et le dictionnaire de la séance.
        """
        print(f"{Colors.LIGHT_PURPLE}==== Ajout d'une seance ====")

        self.ask_check_date()
        self.ask_seance()
        return self.warning_to_main, self.dico_user

    # ===== OK =====
    def ask_check_date(self):
        """
        Demande la date de séance et vérifie son format.

        La date doit contenir deux séparateurs identiques ('-' ou '/'), un jour
        compris entre 1 et 31, un mois compris entre 1 et 12, et une année sur
        2 ou 4 chiffres. Si l'année est sur 2 chiffres, elle est convertie en
        format complet avec le préfixe '20'.

        Returns:
            None: La date validée est stockée dans `self.dico_user["date"]`.
        """
        while True:

            self.date_seance = input(f"{Colors.LIGHT_PURPLE}Veuillez entrer la date de la seance: ")

            # Check nombre de caractères. Min=8: DD/MM/YY ou Max=10: DD/MM/YYYY
            if not(len(self.date_seance) == 8 or len(self.date_seance) == 10):
                print(f"{Colors.RED}Erreur de syntaxe de la date. Le nombre de caractere pour la date est incoherent ")
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
                    case 2: # Année si 2 chiffres rajouter "20". Ex: si année = 26 alors année devient 2026
                        if (len(date_number[index]) == 2):
                            date_number[index] = "20" + date_number[index]
                        elif (len(date_number[index]) == 4):
                            if not date_number[index].startswith("20"):
                                print(f"{Colors.RED}Erreur dans le nombre l'annee. Doit commence par '20'")
                                error_date_flag = True
                                self.warning_to_main = True
                                self.log.log_warning(f"ADD_SEANCE | Problème saisie utilisateur pour l'annee de la "
                                                     f"séance: {date_number[index]}")
                if error_date_flag:
                    break

            if error_date_flag:
                continue

            self.dico_user["date"] = "/".join(date_number)
            return

    # ===== OK =====
    def ask_seance(self):
        """
        Demande à l'utilisateur de saisir une séance complète.

        La méthode collecte successivement le nom de chaque exercice, puis les
        séries, répétitions et charges associées. Les données sont stockées dans
        `self.dico_user["exercices"]`.

        Returns:
            None: Le dictionnaire final est enregistré dans `self.dico_user`.
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

                series_reps_load['series'] = input(f"{Colors.LIGHT_PURPLE}{seance_exercise['name']} "
                                                       f"seance {nb_seance}: Entrez le nombre de series: ")
                series_reps_load['series'] = self.check_user_input_add_seance(series_reps_load['series'], "int")

                series_reps_load["reps"] = input(f"{Colors.LIGHT_PURPLE}{seance_exercise['name']} "
                                                     f"seance {nb_seance}: Entrez le nombre de reps: ")
                series_reps_load["reps"] = self.check_user_input_add_seance(series_reps_load["reps"], "int")

                series_reps_load["loads"] = input(f"{Colors.LIGHT_PURPLE}{seance_exercise['name']} "
                                                  f"seance {nb_seance}: Entrez la charge/poids, en Kg, "
                                                  f"de cette serie: ")
                series_reps_load["loads"] = self.check_user_input_add_seance(series_reps_load["loads"], "float")

                if self.error_seance_flag:
                    print(f"{Colors.RED}Erreur de saisie lors de l'ajout d'une seance. "
                          f"Seance non enregistree{Colors.END}")
                    self.log.log_error(f" ASK SEANCE | Erreur dans l'ajout d'une seance: {series_reps_load}")
                    break

                seance.append(series_reps_load)

                # Choix pour quitter la boucle d'ajout des séances pour un exercice
                continue_add_seance = input(f"{Colors.CYAN}Voulez vous ajouter une autre seance à l'exercice "
                                                 f"{seance_exercise['name']}? oui ou non:  ")
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

    def check_user_input_add_seance(self, variable: str | int, expectedType: str | int | float) -> int | float:
        """
        Vérifie qu'une saisie utilisateur correspond au type attendu.

        La méthode valide les nombres entiers, les chaînes alphabétiques et les
        nombres décimaux au format avec un point. En cas d'erreur, elle active
        `self.error_seance_flag` et renvoie la valeur originale pour permettre
        la journalisation de l'incident.

        Args:
            variable (str | int): Valeur saisie par l'utilisateur.
            expectedType (str | int | float): Type attendu, sous forme de mot-clé
                ou de type utilisé dans l'appel.

        Returns:
            int | float | str: Valeur convertie si la saisie est valide, sinon la
            valeur d'origine.
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

            case "float":
                test_float = variable
                if (variable.isdigit()):
                    # Si le poids correspond à un entier (ex: 20), on le convertit en int
                    self.check_user_input_add_seance(variable=variable, expectedType=int)
                elif (variable.count(".") == 1):
                    # Test présence '.' dans le nombre décimal
                    test_float = variable.split(".")
                else:
                    print(f"{Colors.RED}WARNING!! Veuillez noter UNIQUEMENT des chiffres entiers ou décimaux '.'")
                    self.error_seance_flag = True
                    return variable  # Pour que l'erreur soit logguée

                for case in test_float:
                    if not case.isdigit():
                        print(f"{Colors.RED}WARNING!! Veuillez noter UNIQUEMENT des chiffres entiers ou "
                              f"décimaux '.'")
                        self.error_seance_flag = True
                        return variable  # Pour que l'erreur soit logguée
                return float(variable)


if __name__ == "__main__":
    import json

    test_add_seance = HMI_add_seance(log_name="HMI")
    test_add_seance.ask_check_date()
    # flag_error, dico_user = test_add_seance.hmi()
    # print(test_add_seance.dico_user)

    # with open("test_dico_user.json", "w", encoding="utf-8") as file:
    #     json.dump(dico_user, file, indent=4, ensure_ascii=False)