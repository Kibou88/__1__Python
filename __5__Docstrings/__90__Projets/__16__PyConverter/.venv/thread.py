# thread.py
# --------------
# Purpose:
# Create the thread
# ---------------------------
# Creation date: 2025-07-22
# Modification date: 2025-07-22
# ------------------------------
# Version V1.0.0:

from PySide6.QtCore import QObject, Signal

from API.image import Image, CustomImage
from misc.logs import Logs


class Worker(QObject):

    finished = Signal()  # Va permettre va indiquer que le processus de conversion est finie
    image_converted = Signal(object, bool)  #

    def __init__(self, images_to_convert, quality, size, folder, log_dir="Logs"):
        super().__init__()
        self.images_to_convert = images_to_convert
        self.quality = quality
        self.size = size
        self.folder = folder
        self.logs = Logs(application_name="Thread", log_dir=log_dir)
        self.logs.log_info(f"Thread démarré")
        self.runs = True


    def convert_images(self):
        """
        Convert images
        """
        for image_lw_item in self.images_to_convert:
            if not self.runs:
                self.logs.log_warning("La conversion a été stoppé par l'utilisateur")
            if self.runs and not image_lw_item.processed:
                try:
                    image = CustomImage(path=image_lw_item.text(), folder=self.folder)
                    success = image.reduce_image(size=self.size, quality=self.quality)
                except Exception as e:
                    self.logs.log_error(e)
                else:
                    self.logs.log_info(f"L'image {image_lw_item.text()} a été convertit")
                    self.image_converted.emit(image_lw_item, success)
        self.finished.emit() # Le signal a été mis pour récupérer le signal dans Main Window