"""
Format data
------------------------------
But:
---
Gérer la partie format des données pour être utilisées par SQLite3
Gérer le nombre de données à transmettre, correspond au nombre de "?" dans la requête SQL
----------------------------------------------------------------------------
Date de création: 2026-04-20
Date de modification: 2026-04-20
----------------------------------------------------------------------------
Version PROTOTYPE:


"""

import sys
import sqlite3

class Format_data:
    """

    """

    def __init__(self, data: (list or tuple or dict), test=False):

        self.test = test
        self.data = data

        if(type(self.data) == dict):
            self.format_dico()
        elif(type(self.data) == list or type(self.data) == tuple):
            self.format_liste_tuple()
        else:
            print(f"Format {type(self.data)} non pris en charge")
            sys.exit(1)

    def format_dico(self):
        list_exo_seance = []
        list_datas = []
        list_tables = []

        # ------- Table séance -------
        list_tables.append("seances")
        for i in range(len(self.data["exercices"])):
            list_exo_seance.append((self.data["exercices"][i]["name"]).lower().replace(" ", "_"))

            for j in range(len(self.data["exercices"][i]["seance"])):
                list_tables.append(self.data["exercices"][i]["name"].lower().replace(" ", "_"))
                list_datas.append([self.data["exercices"][i]["seance"][j]["series"],
                                        self.data["exercices"][i]["seance"][j]["reps"],
                                        self.data["exercices"][i]["seance"][j]["loads"]])

        list_datas.insert(0, [self.data["date"], " ".join(list_exo_seance)])

        print(list_tables)
        print(list_datas)

        for table, row in zip(list_tables, list_datas):
            print(table, row)



    def format_liste_tuple(self):
        print("Format liste ou tuple")

    def nbre_interro(self):
        pass
        # if len(self.list_name_colonne) > 1:
        #     interrogations = "?, " * len(self.list_name_colonne)
        #     return interrogations[:-2]
        # elif len(self.list_name_colonne) == 1:
        #     return "?

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
                                    "loads": 30
                                },
                                {
                                    "series": 20,
                                    "reps": 30,
                                    "loads": 40
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

    # print(len(dict_datas["exercices"]))
    # test_list_datas = Format_data(list_datas, test=True)
    test_dict_datas = Format_data(dict_datas, test=True)
    # test_int_datas = Format_data(int_datas, test=True)
