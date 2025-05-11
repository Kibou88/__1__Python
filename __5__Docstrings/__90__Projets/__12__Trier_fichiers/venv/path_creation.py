"""
Projet: Trier fichiers
---------------------
path_creation.py
But: Contient la classe permettant de créer toutes les variables de path
--------------------------------
Date de création: 2025-05-11
Date de modification: 2025-05-11
--------------------------------
Version: 1.0
"""

from pathlib import Path


class Path_Creation:
    """
    A class to manage file and folder paths.

    This class provides methods to create and manage file paths and directory paths,
    including the creation of directories based on year and month.
    """

    def __init__(self, user_path: str, dico_month: dict = None):
        """
        :param user_path: str
            The Path object representing the user's working directory.

        :param dico_month: dict, optional
            The dictionary used for converting month numbers to month names.
            For example, { '01': '01_January', '02': '02_February', ... }.
            If not provided, months will be represented by their numerical values.
        """
        self.user_path = Path(user_path)
        self.dico_month = dico_month

    def file_path(self, file: str) -> Path:
        """
        Create the path including the file to manage and check the presence of extension
        :param file: str
            Name of the file with this extension
        :return: self.file_path: Path
            The absolute path including the file to manage
        """
        self.file_path = self.user_path.joinpath(file)
        if not self.file_path.suffix:
            raise TypeError(f"Le fichier {file} n'as pas d'extension")
        print("Lien OK")
        return self.file_path

    def path_year_month(self, year: int, month: int) -> Path:
        """
        Create the path and folders (if needing) with this architecture (without dico_month conversion):
        user_path/
            ├── year1/
            │   ├── 01/
            │   ├── 02/
            │   ├── ...
            │   └── 12/
            ├── year2/
            │   ├── 01/
            │   ├── 02/
            │   ├── ...
            │   └── 12/
        :param year: int
            Variable corresponding to the year of creation of the file
        :param month: int
            Variable corresponding to the year of creation of the file
        :return: Path
            The absolute path including year and month
        """
        if self.dico_month != None:
            self.path_year_month = self.user_path.joinpath(str(year), self.dico_month.get(str(month)))
        else:
            self.path_year_month = self.user_path.joinpath(str(year),str(month))

        if not self.path_year_month.exists():
            self.path_year_month.mkdir(exist_ok=True, parents=True)
            print(f"Le dossier {self.path_year_month} a ete cree")
        else:
            print(f"Le dossier {self.path_year_month} est deja existant")

        return self.path_year_month


if __name__ == "__main__":
    from constantes.constantes import DICO_MOIS

    user_path = \
        "C:\\Users\\Satoshi\\Desktop\\Code\\__1__Entrainement_Python\\__5__Docstrings\\__90__Projets\\__12__Trier_fichiers\\venv"
    file = "test.jpg"
    year = 2025
    month = 12

    print(Path_Creation(user_path).file_path(file))
    print(Path_Creation(user_path, DICO_MOIS).path_year_month(2025, 12))

    # Test gestion d'erreur si oubie d'extension
    file2 = "test"
    try:
        Path_Creation(user_path).file_path(file2)
    except TypeError as e:
        print(e)
    print("Continuons")