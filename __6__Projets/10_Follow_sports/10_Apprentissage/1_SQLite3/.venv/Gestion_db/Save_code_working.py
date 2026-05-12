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

import sqlite3

from class_colors import Colors

class DataBase:
    """
    Classe contenant la création et la gestion de tables BdD
    """

    def __init__(self, dbName="default.db", dbTableName="default_table"):
        """
        Initialisation de la classe BdD
        :param dbName: Nom de la DB. Si le nom ne contient pas l'extension '.db', il est rajouté.
        :param dbTableName: Nom de la table
        """
        if(dbName.endswith(".db")):
            self.dbName = dbName
        else:
            self.dbName = dbName + ".db"

        self.dbTableName = dbTableName

    # -------- Test OK --------
    def create_table(self, config_colonne=[]):
        """
        Créer une nouvelle table en fonction des paramètres de l'utilisateur.
        :param; self.dbTableName (str): nom de la table
        :param: self.nom_table_colonne (str): forme concaténer des noms de colonnes et leurs critères
        :return:
        """
        print("La table n'existe pas")
        # if (self.check_tables_exists()):
        self.config_colonne = config_colonne
        self.create_column()
        print(f"Table selectionne: {self.dbTableName}")
        with sqlite3.connect(self.dbName) as conn:
            cur = conn.cursor()

            # Activer les clés étrangères dans SQLite
            cur.execute("PRAGMA foreign_keys = ON;")


            cur.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.dbTableName} (
                    {self.table_colonne}
                )
            ''')
            conn.commit()

    # -------- Test OK --------
    def create_column(self) -> str:
        """
        Demande à l'utilisateur le nombre de colonnes, ainsi que les noms et critères pour créer un nouvelle table
        :return: self.nom_table_colonne (str): retourne la forme concaténer des noms de colonnes et leurs critères
        """
        if(self.config_colonne == []):
            nombre_colonne = int(input("Nombre de colonne: "))
            self.liste_table_colonne = []
            for colonne in range(0, nombre_colonne):
                nom_colonne = input("Nom de la colonne + criteres: ")
                self.liste_table_colonne.append(nom_colonne)

            self.table_colonne = ", ".join(self.liste_table_colonne)
        else:
            self.table_colonne = ", ".join(self.config_colonne)

    # ************* A TESTER *************
    def read_table(self):
        """
        Permet de lire la table et de récupérer les données souhaitées
        :param self.dbTableName (str): nom de la table
        :return:
        """
        with sqlite3.connect(self.dbName) as conn:
            cur = conn.cursor()
            cur.execute(f'SELECT * FROM {self.dbTableName} ORDER BY annee')
            resultats = cur.fetchall()
            print(resultats)
            for livre in resultats:
                print(f"ID: {livre[0]}, Titre: {livre[1]}, Auteur: {livre[2]}, Année: {livre[3]}")

    # -------- Test OK --------
    # - Améliorer la gestion d'erreur
    def write_datas_table(self, table_selected: str, date_seance: str, datas: (tuple | list),
                          name_colonne: list, secondary_table=True):
        """
                Permet d'écrire des données dans une table sélectionnée
                :param table_selected (str): Nom de la table à sélectionner
                :param datas (tuple | list): Données à envoyer à la table
                :param name_colonne (list): Nom des colonnes
                :return:
                """
        self.date_seance = date_seance
        print("nom colonne: ", name_colonne)
        if secondary_table:
            name_colonne.insert(0, "seances_id")
            self.recup_primary_id()
            print("nom colonne: ", name_colonne)
            if self.seances_id:
                datas = list(datas)
                datas.insert(0, self.seances_id)

        self.name_colonne = ", ".join(name_colonne)
        self.number_colonne = len(name_colonne)

        # ---- Fait correspondre le nombre de colonne avec le nombre de ? pour la requête SQL ----
        if self.number_colonne > 1:
            nbre_interrogations = "?, " * self.number_colonne
            nbre_interrogations = nbre_interrogations[:-2]
            print(nbre_interrogations)
        elif self.number_colonne == 1:
            nbre_interrogations = "?"

        if not (isinstance(datas, tuple | list)):
            print(f"Mauvais format de fichier. Format envoye: {type(datas)}")
            exit(1)

        with sqlite3.connect(self.dbName) as conn:
            cur = conn.cursor()
            print(datas)
            print(self.name_colonne)
            # try:
            cur.execute(f"INSERT INTO {table_selected} ({self.name_colonne}) VALUES ({nbre_interrogations})", datas)
            conn.commit()
            # except sqlite3.OperationalError as e:
            #     print(f"{Colors.RED}Impossible d'ecrire dans le tableau")
            #     print(e, Colors.END)
            # except:
            #     print(f"{Colors.RED}Erreur sur la sauvegarde{Colors.END}")

    # ************* A TESTER *************
    def show_tables(self, return_nom_table=0) -> list:
        """
        Permet d'afficher les noms des différentes tables de la base de données
        :param return_nom_table (bool): A 1, pour récupérer les tables présentes
        :return: self.names_tables (list): noms des tables de la base de données
        """
        self.names_tables = []
        with sqlite3.connect(self.dbName) as conn:
            cur = conn.cursor()
            cur.execute('SELECT name FROM sqlite_master WHERE type = "table"')
            noms_tables = cur.fetchall()
            # print(noms_tables)
            self.names_tables=["".join(list(nom_table)) for nom_table in noms_tables]
            if(return_nom_table):
                return self.names_tables
            # print(self.names_tables)

    # ************* A TESTER *************
    def check_tables_exists(self) -> bool:
        """
        Vérifie si la table existe ou non
        :return: True: la table n'existe pas
        :return: False: la table n'existe pas
        """
        # self.show_tables()
        if self.dbTableName not in self.names_tables:
            return True
        else:
            print(f"La table {self.dbTableName} existe deja")
            return False

    def recup_primary_id(self):
        """
        Permet de récupérer l'id de la séance présente dans la table "séances"
        :return: self.seances_id (int): Variable contenant la valeur de l'id correspondant à la séance
        """
        with sqlite3.connect(self.dbName) as conn:
            cur = conn.cursor()
            print("Date: ", self.date_seance)
            cur.execute("SELECT id FROM seances WHERE date = ?", (f"{self.date_seance}",))
            result = cur.fetchone()
            if result:
                self.seances_id = result[0]
                print("ID trouve: ", self.seances_id)
            else:
                print("Client non trouve")

if __name__ == "__main__":

    exo_date = '28/03/26'
    test_datas = [('28/03/26', 'squats fentes_avant'), ("5", "10", "15")]

    list_name_table = ["seances", "squats"]

    config_colonne = [
                    ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                      "date TEXT NOT NULL",
                      "exercices TEXT NOT NULL"],
                      ["seances_id INTEGER",
                       "series INTEGER NOT NULL",
                       "reps INTEGER NOT NULL",
                       "loads INTEGER",
                       "FOREIGN KEY (seances_id) REFERENCES seances (id)"]
                      ]


    name_colonne = [
                    ["date", "exercices"],
                    ["series", "reps", "loads"]
                    ]
    #  ---- Fonctionne sans FOREIGN KEY ----
    for i in range(len(list_name_table)):
        # print(list_name_table[i])
        # print(test_datas[i])
        database_seance = DataBase(dbName="test_db_seance.db", dbTableName=list_name_table[i])
        database_seance.create_table(config_colonne=config_colonne[i])
        secondary_table = False if i == 0 else True

        database_seance.write_datas_table(table_selected=list_name_table[i],
                                          date_seance=exo_date,
                                          datas = test_datas[i],
                                          name_colonne=name_colonne[i],
                                          secondary_table=secondary_table)
        print("Table ok: ", list_name_table[i])