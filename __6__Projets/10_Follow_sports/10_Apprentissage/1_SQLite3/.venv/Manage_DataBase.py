"""
Test Gestion Base de données
------------------------------
But:
---
Tester la création et la gestion de tables BdD au travers d'une classe dédiée
----------------------------------------------------------------------------
Date de création: 2026-01-19
Date de modification: 2026-01-19
----------------------------------------------------------------------------
Version PROTOTYPE:


"""
import os
import sqlite3
import sys

from class_colors import Colors

class DataBase:
    """
    Classe contenant la création et la gestion de tables BdD
    """

    def __init__(self, dbName="default.db"):
        """
        Initialisation de la classe BdD
        :param dbName (str): Nom de la DB. Si le nom ne contient pas l'extension '.db', il est rajouté.
        """
        if not (dbName.endswith(".db")):
            dbName = dbName + ".db"
        elif dbName == "":
            dbName = "default.db"
        self.dbName = dbName

    def check_or_create_db(self):
        """
        Vérifie si la database demandée est présente, sinon création de la db.
        Ensuite, connexion à la db voulue
        :return:
        """
        try:
            self.conn = sqlite3.connect(self.dbName)
            self.cur = self.conn.cursor()
            return True
        except Exception as e:
            print(e)
            return False
        except PermissionError:
            print(f"Permissions insuffisantes pour acceder a {self.dbName}")
            return False



    def db_close(self):
        """
        Déconnexion de la db
        :return:
        """
        self.conn.close()

    def manage_table(self):
        """
        Vérifie la présence de la table voulue dans la db, si absente elle sera créée
        :return:
        """
        query = """
            SELECT name FROM sqlite_master WHERE type='table' AND name=?
            """
        self.cur.execute(query, (self.table_name,))
        if self.cur.fetchall() == []:
            print("La table n'existe pas")
            print(f"Creation de la table: {self.table_name}")
            if self.define_columns():

                if self.foreign_key_activated:
                    self.cur.execute("PRAGMA foreign_keys = ON;")

                self.cur.execute(f'''
                                CREATE TABLE {self.table_name} 
                                (
                                    {(", ").join(self.config_colonne)}
                                )
                                ''')
                return True
            else:
                print("Liste colonne non recue")
                print("table non creee")
                return False
        else:
            print("La table existe")
            return True


    def define_columns(self):
        """
        Permet de définir les différentes colonnes et leurs caractéristiques SQL
        Gestion du format pour être reconnu par SQL => A FAIRE PLUS TARD
        :return:
        """
        if self.config_colonne== "" or self.config_colonne == [] or self.config_colonne == {}:
            print("Aucun critère de colonne envoye")
            return False
        else:
            print("Liste recu")
            return True

    def nbre_interrogations(self):
        # ---- Fait correspondre le nombre de colonne avec le nombre de ? pour la requête SQL ----
        self.extract_colonne_name()
        if len(self.list_name_colonne) > 1:
            interrogations = "?, " * len(self.list_name_colonne)
            return interrogations[:-2]
        elif len(self.list_name_colonne) == 1:
            return "?"

    def extract_colonne_name(self):
        self.list_name_colonne = []
        for colonne in self.config_colonne:
            if not colonne.split(" ")[0] == "id":
                self.list_name_colonne.append((colonne.split(" "))[0])

        self.name_colonne = (', ').join(self.list_name_colonne)

    def write_data(self, table_name, config_colonne, datas, foreign_key_activated):
        self.table_name = table_name
        self.config_colonne = config_colonne
        self.datas = datas
        self.foreign_key_activated = foreign_key_activated

        # self.extract_colonne_name()

        if self.check_or_create_db(): # Vérification aucune erreur de création ou accès à la db
            print("Connecte")
            if self.manage_table():
                self.extract_colonne_name()
                print("nom colonne: ", self.name_colonne)
                print("nbre ?: ", self.nbre_interrogations())
                try:

                    self.cur.execute(
                        f"INSERT INTO {self.table_name} ({self.name_colonne}) "
                        f"VALUES ({self.nbre_interrogations()})",
                        datas)
                    self.conn.commit()

                except sqlite3.OperationalError as e:
                    print(f"{Colors.RED}Impossible d'ecrire dans le tableau")
                    print(e, Colors.END)
                except sqlite3.ProgrammingError as e:
                    print(f"{Colors.RED}Impossible d'ecrire dans le tableau")
                    print(e, Colors.END)
                except AttributeError as e:
                    print(f"{Colors.RED}Erreur sur l'attribut d'un objet")
                    print(e, Colors.END)
                except:
                    print(f"{Colors.RED}Erreur de sauvegarde des donnees. Probleme detecte{Colors.END}")

                self.db_close()
                sys.exit()
            else:
                self.db_close()
                sys.exit(1)
        else:
            print("Not Connected")
            sys.exit(1)


if __name__ == "__main__":

    test_datas = ['27/03/26', 'squats fentes_avant']
    config_colonne = ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                      "date TEXT NOT NULL",
                      "exercices TEXT NOT NULL"]
    name_colonne = ["date", "exercices"]

    exo_date = '28/03/26'
    test_datas2 = [('28/03/26', 'squats fentes_avant'), ("5", "10", "15")]

    list_name_table2 = ["seances", "squats"]

    config_colonne2 = [
                    ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                      "date TEXT NOT NULL",
                      "exercices TEXT NOT NULL"],
                      ["seances_id INTEGER",
                       "series INTEGER NOT NULL",
                       "reps INTEGER NOT NULL",
                       "loads INTEGER",
                       "FOREIGN KEY (seances_id) REFERENCES seances (id)"]
                      ]


    name_colonne2 = [
                    ["date", "exercices"],
                    ["series", "reps", "loads"]
                    ]


    test_db = DataBase("Test")
    test_db.write_data(table_name="test",
                       config_colonne=config_colonne,
                       datas=test_datas,
                       foreign_key_activated=False)

