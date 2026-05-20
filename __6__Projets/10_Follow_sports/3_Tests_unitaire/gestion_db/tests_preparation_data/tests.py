import unittest
import os
import sqlite3
import time
from unittest import TextTestRunner
from pathlib import Path
from datetime import datetime

from gestion_db.preparation_data import Preparation_data


def connect_db(db_file: str):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
    return conn, cursor

def close_db(conn):
    conn.close()

class Tests_preparation_data(unittest.TestCase):
    def setUp(self) -> None:
        self.int_data = 5
        self.list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.dict_data = {
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
        self.test = True

    def tearDown(self) -> None:
        pass

    def test_type_data(self):
        with self.assertRaises(TypeError) as context:
            Preparation_data(self.int_data, test = self.test).detect_type()
        self.assertEqual(str(context.exception), f"Format {type(self.int_data)} non pris en charge")

        with self.assertRaises(Exception) as context:
            Preparation_data(self.list_data, test = self.test).detect_type()
        self.assertEqual(str(context.exception), f"Format {type(self.list_data)} non implemente dans "
                                                 f"cette version")

    def test_prep_dict_data(self):
        zip_dict_data = Preparation_data(data = self.dict_data, test = self.test).detect_type()

        print("type: ", type(zip_dict_data))
        print("data zip: ", zip_dict_data)
        with open("output_prep_data.txt", "w+") as f:
            f.write("Test:\n")
            print("Affichage contenu: ")
            for table, row, nb_fields in zip_dict_data:
                f.writelines(table)
                f.write('\t')
                f.writelines(str(row))
                f.write('\t')
                f.writelines(nb_fields)
                f.write("\n")
                print(table, row, nb_fields)

if __name__ == '__main__':
    unittest.main()
