# image.py
# --------------
# Purpose:
# Class CustomImage
# ---------------------------
# Creation date: 2025-07-17
# Modification date: 2025-07-17
# ------------------------------
# Version V1.0.0:

import os
import sys

from PIL import Image

class CustomImage:
    def __init__(self, path, folder="reduced"):
        self.image = Image.open(path)
        self.width, self.height = self.image.size
        self.path = path
        # os.path.dirname permet de récupérer le nom du dossier où est le fichier
        # os.path.basename permet de récupérer le nom + extension du fichier
        self.reduced_path = os.path.join(os.path.dirname(self.path), folder, os.path.basename(self.path))

    def reduce_image(self, size=0.5, quality=75):
        """
        Convert the image depends of the size and quality values
        :param size: (float) size of the image in pixels
        :param quality: (int) quality of the image
        """
        new_width = round(self.width * size)
        new_height = round(self.height * size)
        # Image.LANCZOS: Permet de garantir la qualité de l'image lors de la réduction (lent, excellente qualité)
        self.image = self.image.resize((new_width, new_height), Image.LANCZOS)

        parent_dir = os.path.dirname(self.reduced_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        self.image.save(self.reduced_path, 'JPEG', quality=quality)
        return os.path.exists(self.reduced_path)
if __name__ == '__main__':
    test_image = CustomImage(path=os.path.join(os.path.dirname(__file__), "test", "test.jpg"))
    test_image.reduce_image()