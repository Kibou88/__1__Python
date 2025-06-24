from uuid import uuid4
import os
import json
from API.constants import NOTES_DIR

class Note:
    def __init__(self, title="", contents="", uuid=None):
        #uuid: Unique IDentifer
        self.title = title
        self.contents = contents
        self.uuid = (str(uuid4()) if uuid is None else uuid)

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

    def save(self):
        """
        Permet de sauvegarder la note à l'emplacement path
        """
        if not os.path.exists(NOTES_DIR):
            os.makedirs(NOTES_DIR)

        data = {
            "title": self.title,
            "contents": self.contents
        }
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def delete(self):
        """
        Supprime une note en fonction de son UUID et gère l'exception si la note n'as pas été trouvé
        :return:
        True ou Fale: Si la note a été supprimé ou non
        """
        try:
            os.remove(self.path)
        except FileNotFoundError:
            print("File doesn't exist")
            return False
        else:
            print("File deleted")
            return True

if __name__ == "__main__":
    note = Note("Note", contents="Test", uuid = "6c8a37b3-b455-4b94-930d-c4886af9495d")
    print(note.uuid)
    print(repr(note))
    # Si la méthode a un décorateur "@property" ne pas inclure les () à la fin de "path"
    print(note.path)
    note.save()
    note.uuid = "6c8a37b3-b455-4b94-930d-c4886af9495d"
    note.delete()