from uuid import uuid4
import os
from API.constants import NOTES_DIR

class Note:
    def __init__(self, title="", contents="", uuid=None):
        #uuid: Unique IDentifer
        self.title = title
        self.contents = contents
        self.uuid = str(uuid4())

    @property
    def path(self):
        """
        Concaténer le chemin de note avec le numéro unique uuid et au format json
        :param:
        NOTES_DIR (str): Chemin défini dans le fichier constants
        :return:
        (str) Chemin de la note avec l'extenson json
        """
        return os.path.join(NOTES_DIR, self.uuid + ".json")

    def __repr__(self):
        return f"Note: {self.title}, {self.uuid})"

    def __str__(self):
        return self.title

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, str):
            self._content = value
        else:
            raise TypeError(f"Content must be of type str")



if __name__ == "__main__":
    note = Note("Note", contents="Test")
    print(note.uuid)
    print(repr(note))
    # Si la méthode a un décorateur "@property" ne pas inclure les () à la fin de "path"
    print(note.path)