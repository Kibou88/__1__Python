# Trieur de fichiers
#
# But:
# Permettre le tri des différents fichiers
# mp3, wav, flac: Musique
# avi, mp4, gif: Vidéos
# bmp, png, jpg: Images
# txt, pptx, csv, xls, odp, pages: Documents
# autres: Divers
##########################################
from pathlib import Path
from pprint import pprint

# Dico pour répertorié tout les types de fichiers
typeFiles={
    ".mp3":"Musique",
    ".wav":"Musique",
    ".flac":"Musique",
    ".avi":"Vidéos",
    ".mp4":"Vidéos",
    ".gif":"Vidéos",
    ".bmp":"Images",
    ".png":"Images",
    ".jpg":"Images",
    ".txt":"Documents",
    ".pptx":"Documents",
    ".csv":"Documents",
    ".xls":"Documents",
    ".odp":"Documents",
    ".pages":"Documents"
}
#     "Musique":["mp3","wav","flac"],
#     "Vidéos":["avi","mp4", "gif"],
#     "Images":["bmp","png","jpg"],
#     "Documents":["txt","pptx","csv","xls","odp","pages"],
# }

chemin = Path.cwd() # Retourne le chemin actuel
cheminData = chemin / "data" # Chemin dans le dossier "data"

# for i in typeFiles.keys(): # Permet de boucler sur chaque clé du dico
#     cheminDataType= cheminData / i
#     cheminDataType.mkdir(exist_ok=True) # Va créer le dossier en fonction du type de fichier SI il existe déjà => ne rien faire

files=[f for f in cheminData.iterdir() if f.is_file()] # Répertorie SEULEMENT les fichiers
for f in files:
    output_dir = cheminData / typeFiles.get(f.suffix,"Divers")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)
