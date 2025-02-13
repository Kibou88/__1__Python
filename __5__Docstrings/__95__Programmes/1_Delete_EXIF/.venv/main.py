# Delete EXIF
# But: Supprimer les données EXIF d'une photo
#----------------------------------------------
# Date de création: 2025-02-13
# Date de modification: 2025-02-13
#-----------------------------------------------
import sys
from PIL import Image
from pathlib import Path

def remove_exif_data(input_image_path, output_image_path):
    # Ouvrir l'image
    image = Image.open(input_image_path)

    # Supprimer les données EXIF
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)

    # Sauvegarder l'image sans les données EXIF
    image_without_exif.save(output_image_path)

if __name__ == "__main__":
    input_image_path = sys.argv[0]
    path_input_image = Path(input_image_path)
    folder_parent = path_input_image.parent
    print(input_image_path)
    print(path_input_image)
    print(folder_parent)
input_image_path = 'chemin/vers/image_avec_exif.jpg'
output_image_path = 'chemin/vers/image_sans_exif.jpg'
remove_exif_data(input_image_path, output_image_path)
