"""
Test unitaire - Module Manage Database (DataBase)
---------------------------------------------------
But:
----
Tester UNIQUEMENT la classe DataBase (gestionDB/manage_database.py) en isolant
les dépendances externes (Logs, Format_data, Create_table) par des mocks.

Les interactions SQLite elles-mêmes sont testées avec une vraie base de données
temporaire (fichier .db dans un dossier temporaire) afin de valider le
comportement réel des requêtes SQL générées par le module.

IMPORTANT:
----------
L'import ci-dessous suppose que la classe DataBase se trouve dans
"gestionDB.manage_database". Si le fichier réel porte un autre nom,
adapte uniquement la ligne d'import correspondante.
----------------------------------------------------------------------------
Date de création: 2026-07-03
----------------------------------------------------------------------------
"""

import os
import sys
import shutil
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Permet de lancer les tests depuis "3_Tests" sans dépendre d'un PYTHONPATH
# configuré manuellement : on ajoute "2_Code" (dossier parent contenant
# le package gestionDB) au sys.path si besoin.
CODE_DIR = Path(__file__).resolve().parent / "2_Code" / ".venv" / "gestionDB"
if CODE_DIR.exists() and str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from gestionDB.manage_database import DataBase


class BaseDataBaseTestCase(unittest.TestCase):
    """
    Classe de base: prépare un dossier temporaire pour les fichiers .db
    et les logs, et le nettoie après chaque test.
    """

    def setUp(self):
        self.tmp_dir = Path(tempfile.mkdtemp(prefix="test_manage_db_"))
        self.db_path = self.tmp_dir / "test.db"
        self.log_path = self.tmp_dir / "Test_log"

        self.valid_data = {
            "date": "28/03/26",
            "exercices": [
                {
                    "name": "Squats",
                    "seance": [
                        {"series": 10, "reps": 20, "loads": 30.5},
                    ],
                }
            ],
        }

        # Patch de Logs pour toutes les instances de DataBase créées dans les tests
        self.logs_patcher = patch("gestionDB.manage_database.Logs")
        self.mock_logs_cls = self.logs_patcher.start()
        self.mock_log_instance = MagicMock()
        self.mock_logs_cls.return_value = self.mock_log_instance

    def tearDown(self):
        self.logs_patcher.stop()
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def make_db(self, dbName=None, data_to_send=None, test=True):
        return DataBase(
            dbName=str(dbName if dbName is not None else self.db_path),
            data_to_send=self.valid_data if data_to_send is None else data_to_send,
            log_name="Test_log_name",
            log_path=self.log_path,
            test=test,
        )


class TestInit(BaseDataBaseTestCase):
    """Tests du constructeur __init__"""

    def test_ajout_extension_db_si_absente(self):
        db = self.make_db(dbName=self.tmp_dir / "sans_extension")
        self.assertTrue(db.dbName.endswith(".db"))

    def test_extension_db_deja_presente_non_dupliquee(self):
        db = self.make_db(dbName=self.tmp_dir / "avec_extension.db")
        self.assertTrue(db.dbName.endswith(".db"))
        self.assertFalse(db.dbName.endswith(".db.db"))

    def test_data_to_send_vide_dict_leve_valueerror_en_mode_test(self):
        with self.assertRaises(ValueError):
            self.make_db(data_to_send={}, test=True)

    def test_data_to_send_vide_liste_leve_valueerror_en_mode_test(self):
        with self.assertRaises(ValueError):
            self.make_db(data_to_send=[], test=True)

    def test_data_to_send_vide_chaine_leve_valueerror_en_mode_test(self):
        with self.assertRaises(ValueError):
            self.make_db(data_to_send="", test=True)

    def test_data_to_send_vide_sans_mode_test_ne_leve_pas(self):
        # test=False : pas d'exception, mais error_to_main doit passer à True
        db = self.make_db(data_to_send={}, test=False)
        self.assertTrue(db.error_to_main)
        self.mock_log_instance.log_error.assert_called()

    def test_data_to_send_valide_error_to_main_reste_false(self):
        db = self.make_db(data_to_send=self.valid_data, test=True)
        self.assertFalse(db.error_to_main)

    def test_attributs_correctement_assignes(self):
        db = self.make_db(data_to_send=self.valid_data, test=True)
        self.assertEqual(db.data_to_send, self.valid_data)
        self.assertEqual(db.log_name, "Test_log_name")
        self.assertEqual(db.log_path, self.log_path)
        self.assertFalse(db.test is False)  # test=True passé explicitement


class TestAccessDb(BaseDataBaseTestCase):
    """Tests de access_db()"""

    def test_access_db_cree_connexion_et_curseur(self):
        db = self.make_db()
        db.access_db()
        self.assertIsInstance(db.conn, sqlite3.Connection)
        self.assertIsInstance(db.cur, sqlite3.Cursor)
        db.conn.close()

    def test_access_db_cree_le_fichier_db(self):
        db = self.make_db(dbName=self.tmp_dir / "nouvelle_db.db")
        db.access_db()
        db.conn.close()
        self.assertTrue(os.path.exists(db.dbName))


class TestDbSaveAndClose(BaseDataBaseTestCase):
    """Tests de db_save_and_close()"""

    def test_commit_et_close_appeles(self):
        db = self.make_db()
        db.access_db()
        db.conn = MagicMock()
        db.db_save_and_close()
        db.conn.commit.assert_called_once()
        db.conn.close.assert_called_once()


class TestRequestWriteData(BaseDataBaseTestCase):
    """Tests de request_write_data()"""

    def _create_seances_table(self, db):
        db.cur.execute(
            "CREATE TABLE seances (id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "date TEXT, exercices TEXT)"
        )
        db.conn.commit()

    def _create_exercice_table(self, db, table_name="squats"):
        db.cur.execute(
            f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "seances_id INTEGER, series INTEGER, reps INTEGER, loads_kg REAL)"
        )
        db.conn.commit()

    def test_ecriture_table_seances(self):
        db = self.make_db()
        db.access_db()
        self._create_seances_table(db)

        db.request_write_data("seances", ["28/03/26", "Squats"], "?, ?")

        db.cur.execute("SELECT date, exercices FROM seances")
        row = db.cur.fetchone()
        self.assertEqual(row, ("28/03/26", "Squats"))
        db.conn.close()

    def test_ecriture_table_exercice_insere_id_seance(self):
        db = self.make_db()
        db.access_db()
        self._create_seances_table(db)
        self._create_exercice_table(db, "squats")

        db.cur.execute("INSERT INTO seances (date, exercices) VALUES (?, ?)",
                        ("28/03/26", "Squats"))
        db.conn.commit()

        db.request_write_data("squats", [10, 20, 30.5], "?, ?, ?, ?")

        db.cur.execute("SELECT seances_id, series, reps, loads_kg FROM squats")
        row = db.cur.fetchone()
        self.assertEqual(row, (1, 10, 20, 30.5))
        db.conn.close()


class TestCheckOrCreateTable(BaseDataBaseTestCase):
    """Tests de check_or_create_table()"""

    @patch("gestionDB.manage_database.Create_table")
    def test_table_deja_existante_create_table_non_appele(self, mock_create_table_cls):
        db = self.make_db()
        db.access_db()
        db.cur.execute("CREATE TABLE seances (id INTEGER PRIMARY KEY, date TEXT, exercices TEXT)")
        db.conn.commit()

        db.check_or_create_table("seances")

        mock_create_table_cls.assert_not_called()
        # la connexion doit avoir été rouverte par access_db() en fin de méthode
        self.assertIsInstance(db.conn, sqlite3.Connection)
        db.conn.close()

    @patch("gestionDB.manage_database.Create_table")
    def test_table_seances_absente_appelle_creation_typeTable_2(self, mock_create_table_cls):
        mock_instance = MagicMock()
        mock_create_table_cls.return_value = mock_instance

        db = self.make_db()
        db.access_db()

        db.check_or_create_table("seances")

        mock_create_table_cls.assert_called_once_with(
            dbName=db.dbName, log_name=db.log_name, log_path=db.log_path
        )
        mock_instance.creation_type_table.assert_called_once_with(
            tableName="seances", typeTable=2
        )
        db.conn.close()

    @patch("gestionDB.manage_database.Create_table")
    def test_table_exercice_absente_appelle_creation_typeTable_3(self, mock_create_table_cls):
        mock_instance = MagicMock()
        mock_create_table_cls.return_value = mock_instance

        db = self.make_db()
        db.access_db()

        db.check_or_create_table("squats")

        mock_instance.creation_type_table.assert_called_once_with(
            tableName="squats", typeTable=3
        )
        db.conn.close()


class TestCatchIdKey(BaseDataBaseTestCase):
    """Tests de catch_id_key()"""

    def test_retourne_dernier_id_insere(self):
        db = self.make_db()
        db.access_db()
        db.cur.execute("CREATE TABLE seances (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                        "date TEXT, exercices TEXT)")
        db.cur.executemany(
            "INSERT INTO seances (date, exercices) VALUES (?, ?)",
            [("28/03/26", "Squats"), ("29/03/26", "Fentes")],
        )
        db.conn.commit()

        last_id = db.catch_id_key()

        self.assertEqual(last_id, 2)
        db.conn.close()


class TestProcessToWriteData(BaseDataBaseTestCase):
    """Tests de process_to_write_data() - orchestration complète"""

    @patch("gestionDB.manage_database.Create_table")
    @patch("gestionDB.manage_database.Format_data")
    def test_process_succes_ecriture_complete(self, mock_format_data_cls, mock_create_table_cls):
        # Prépare les tables en amont pour éviter le passage par Create_table (mocké, ne crée rien réellement)
        setup_db = self.make_db()
        setup_db.access_db()
        setup_db.cur.execute(
            "CREATE TABLE seances (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, exercices TEXT)"
        )
        setup_db.cur.execute(
            "CREATE TABLE squats (id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "seances_id INTEGER, series INTEGER, reps INTEGER, loads_kg REAL)"
        )
        setup_db.conn.commit()
        setup_db.conn.close()

        mock_format_instance = MagicMock()
        mock_format_instance.detect_type.return_value = (
            [
                ("seances", ["28/03/26", "Squats"], "?, ?"),
                ("squats", [10, 20, 30.5], "?, ?, ?, ?"),
            ],
            False,
        )
        mock_format_data_cls.return_value = mock_format_instance

        db = self.make_db()
        error_to_main = db.process_to_write_data()

        self.assertFalse(error_to_main)
        mock_create_table_cls.assert_not_called()

        conn = sqlite3.connect(db.dbName)
        cur = conn.cursor()
        cur.execute("SELECT date, exercices FROM seances")
        self.assertEqual(cur.fetchone(), ("28/03/26", "Squats"))
        cur.execute("SELECT seances_id, series, reps, loads_kg FROM squats")
        self.assertEqual(cur.fetchone(), (1, 10, 20, 30.5))
        conn.close()

    @patch("gestionDB.manage_database.Format_data")
    def test_process_exception_geree_et_error_to_main_true(self, mock_format_data_cls):
        mock_format_instance = MagicMock()
        mock_format_instance.detect_type.side_effect = Exception("Erreur simulee")
        mock_format_data_cls.return_value = mock_format_instance

        db = self.make_db()
        error_to_main = db.process_to_write_data()

        self.assertTrue(error_to_main)
        self.mock_log_instance.log_error.assert_called()


if __name__ == "__main__":
    unittest.main()