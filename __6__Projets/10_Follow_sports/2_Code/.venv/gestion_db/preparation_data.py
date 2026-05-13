"""
Preparation data
------------------------------
But:
---
Gérer la partie format des données pour être utilisées par SQLite3
Gérer le nombre de données à transmettre, correspond au nombre de "?" dans la requête SQL
----------------------------------------------------------------------------
Date de création: 2026-04-20
Date de modification: 2026-05-06
----------------------------------------------------------------------------
Version V1:
"""

import sys
import sqlite3

class Preparation_data:
    """
    Gestion du formattage des données pour être utilisées dans les requêtes SQL
    Gestion du nombre de champ à transmettre: nombre de "?" dans les requêtes SQL
    /!\Pris en charge seulement du type dict/!\
    """

    def __init__(self, data: (list or tuple or dict), test=False):

        self.test = test
        self.data = data


    def detect_type(self: (dict or list or tuple)) -> zip:
        """
        Oriente les données à formatter dans la méthode appropriée en fonction de son type
        Si les données sont du type 'dico' => méthode self.format_dico()
        Si les données sont du type 'list' ou 'tuple' => méthode self.format_liste_tuple() NON CREEE
        :return: self.zip_tables_data_fields (zip): Formattage des données de type 'dico' en listes pour les
                                                    requêtes SQL
        """
        if (type(self.data) == dict):
            self.format_dico()
            if not self.test:
                return self.zip_tables_data_fields
        elif (type(self.data) == list or type(self.data) == tuple):
            self.format_liste_tuple()
        else:
            print(f"Format {type(self.data)} non pris en charge")
            sys.exit(1)

    def format_dico(self) -> zip:
        """
        Formatte les données de type 'dico'
        :return: self.zip_tables_data_fields (zip): Formattage des données de type 'dico' en listes pour les
                                                    requêtes SQL
        """
        self.list_exo_seance = []
        self.list_datas = []
        self.list_tables = []
        self.list_nb_fields = []

        # ------- Table séance -------
        self.list_tables.append("seances")
        for i in range(len(self.data["exercices"])):
            self.list_exo_seance.append((self.data["exercices"][i]["name"]).lower().replace(" ", "_"))

            for j in range(len(self.data["exercices"][i]["seance"])):
                self.list_tables.append(self.data["exercices"][i]["name"].lower().replace(" ", "_"))
                self.list_datas.append((self.data["exercices"][i]["seance"][j]["series"],
                                        self.data["exercices"][i]["seance"][j]["reps"],
                                        self.data["exercices"][i]["seance"][j]["loads"]))

        self.list_datas.insert(0, (self.data["date"], " ".join(self.list_exo_seance)))

        print(self.list_tables)
        # Compte le nombre de champs utiles par rapport aux données
        self.list_nb_fields = [self.nbre_interro(self.list_tables[i], self.list_datas[i])
                               for i in range(len(self.list_datas))]

        self.zip_tables_data_fields = zip(self.list_tables, self.list_datas, self.list_nb_fields)

        if self.test:

            for table, row, nb_fields in self.zip_tables_data_fields:
                print(table, row, nb_fields)


    # -------------------- A CODER --------------------
    def format_liste_tuple(self):
        """
        A CODER
        :return:
        """
        print("Format liste ou tuple")

    def nbre_interro(self, table_name: str, fields: int) -> str:
        """
        Définit le nombre de champs à remplir en fonction de la table correspondante
        :param table_name (str): Nom de la table
        :param fields (int): Nombre de colonnes (champs) à remplir
        :return: interrogations (str): Format du nombre de champ pour la requête SQL
                                    Format: "?, ?, ...., ?"
        """
        if not (table_name == "seances"):
            interrogations = "?, " * (len(fields)+1) # Ajout du champ seances_id pour la FOREIGN KEY
        else:
            interrogations = "?, " * len(fields)
        return interrogations[:-2]

if __name__ == "__main__":
    list_datas = [('28/03/26', 'squats fentes_avant'), ("5", "10", "15")]
    dict_datas = {
                    "date": "28/03/26",
                    "exercices": [
                        {
                            "name": "Squats",
                            "seance": [
                                {
                                    "series": 10,
                                    "reps": 20,
                                    "loads": 30.5
                                },
                                {
                                    "series": 20,
                                    "reps": 30,
                                    "loads": 40.0
                                }
                            ]
                        },
                        {
                            "name": "Fentes avant",
                            "seance": [
                                {
                                    "series": 10,
                                    "reps": 20,
                                    "loads": 35
                                }
                            ]
                        }
                    ]
                }
    int_datas = 10


    # test_list_datas = Format_data(list_datas, test=True)
    test_dict_datas = Preparation_data(dict_datas, test=True).detect_type()

    test2_dict_datas = Preparation_data(dict_datas).detect_type()
    print("------------------------------")
    print("Test 2:")
    with open("output_prep_data.txt", "w+") as f:
        f.write("Test 2:\n")

        for table, row, nb_fields in test2_dict_datas:
            f.writelines(table)
            f.write('\t')
            f.writelines(str(row))
            f.write('\t')
            f.writelines(nb_fields)
            f.write("\n")
            print(table, row, nb_fields)

        # f.write("------------------------------n")
        # f.write("Test 3:\n")
        # list_dict_tables = zip(*test_dict_datas)
        # print("Test 3: ")
        # f.write(list_dict_tables)
        f.close()
        # print(list_dict_tables)
    # test_int_datas = Preparation_data(int_datas, test=True)


