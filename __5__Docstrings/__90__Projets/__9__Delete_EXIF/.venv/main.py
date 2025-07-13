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
    input_image_path = sys.argv[1]
    path_input_image = Path(input_image_path)
    folder_parent = path_input_image.parent
    name_input = path_input_image.stem
    name_output = name_input + "_modified" + path_input_image.suffix
    output_image_path = folder_parent / name_output

    print(input_image_path)
    print(output_image_path)
    print(folder_parent)
    try:
        remove_exif_data(input_image_path, output_image_path)
    except:
        print("Problème suppression exif")