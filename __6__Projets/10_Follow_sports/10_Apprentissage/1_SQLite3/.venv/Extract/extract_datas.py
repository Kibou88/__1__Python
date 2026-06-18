"""
Extract Base de Données
---------------------------
But:
Extraire les données d'une table et les afficher
"""
import sqlite3

class Extract_datas():

    def __init__(self, database: str):
        if database.endswith('.db'):
            self.database = database
            self.dict_extract = {}
        else:
            self.database = database + ".db"

    def connexion(self):
        # Étape 1: Connexion
        with sqlite3.connect(self.database) as self.conn:  # Context manager auto-ferme
            self.cur = self.conn.cursor()

    def db_save_and_close(self):
        """
        Sauvegarde et déconnexion de la db
        """
        self.conn.commit()
        self.conn.close()

    def list_items_table_seances(self):
        self.connexion()
        self.cur.execute("SELECT * FROM seances ORDER BY id")
        resultats_seances = self.cur.fetchall()
        print("Listes des seances:")
        for seance in resultats_seances:
            print(f"id: {seance[0]}, date: {seance[1]}, exercices: {seance[2]}")
        user_selection = input("Choix de la seance: ")
        self.dict_extract["date"] = str(resultats_seances[int(user_selection)-1][1])
        self.dict_extract["exercices"] = []

        print("Donc votre selection est: ", resultats_seances[int(user_selection)-1])
        # (1, '23/05/2026', 'squats biceps')
        # list_seance = list(resultats_seances[int(user_selection)-1])
        listes_exos = list(resultats_seances[int(user_selection)-1])[2].split(" ")
        print("Listes des exos: ", listes_exos)
        for table_exo in listes_exos:
            dict_exercices = {}
            self.cur.execute(f"SELECT * FROM {table_exo} WHERE seances_id = {int(user_selection)}")


            listes_seance = self.cur.fetchall()
            print("Liste des exos: ", listes_seance)
            # Output: [(3, 5, 10, 20.0)]
            dict_exercices["name"] = table_exo.capitalize()
            dict_exercices["seances"] = []
            for index, seance in enumerate(listes_seance):
                # dict_seance = {}
                # dict_seance[str(index)] = (f"{seance[1]} séries de {seance[2]} reps à "
                #                                                      f"{seance[3]} Kg")
                # dict_exercices["seances"].append(dict_seance)
                dict_exercices["seances"].append(f"{seance[1]} séries de {seance[2]} reps à "
                                                                     f"{seance[3]} Kg")
            self.dict_extract["exercices"].append(dict_exercices)
        self.db_save_and_close()
        print(self.dict_extract)
        return self.dict_extract


    def list_all_tables(self):
        self.connexion()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
        tables = self.cur.fetchall()
        print("Tables de la bd: ", tables)
        self.db_save_and_close()

    def other(self):
        pass
        # Récupérer les colonnes d'une table
        # for table in tables:
        #     print(table[0])
            # self.cur.execute(f"PRAGMA table_info({table[0]})")
            # table_colonnes = self.cur.fetchall()
            # print("Colonne: ", table_colonnes)
            # output pour la table seances:
            # Colonne:  [(0, 'id', 'INTEGER', 0, None, 1), (1, 'date', 'TEXT', 1, None, 0), (2, 'exercices', 'TEXT', 1, None, 0)]
            # 0: Numéro de la colonne
            # 1: Nom de la colonne
            # 2: Type de la colonne
            # 3: 1 si la colonne ne peut pas être NOT NULL, sinon 0
            # 4: valeur par défaut(default value) (NONE: aucune valeur par défaut)
            # 5: pk à 1 veut dire que c'est la clé primaire, sinon 0

            # Récupère la dernière ligne
            # self.cur.execute('SELECT * FROM seances ORDER BY id DESC LIMIT 1')
            # last_ligne = self.cur.fetchall()
            # print("Ligne: ", last_ligne)
            # cur.execute('SELECT * FROM seances ORDER BY id')
            # resultats_seances = cur.fetchall()
            #
            # print(resultats_seances)
            # for ligne in resultats_seances:
            #     print(f"id {ligne[0]}, date {ligne[1]}, exercices {ligne[2]}")

if __name__ == "__main__":
    test = Extract_datas("tests.db").list_items_table_seances()
    print(test)