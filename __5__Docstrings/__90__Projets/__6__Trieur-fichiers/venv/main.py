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
EXTENSIONS_MAPPING={
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

BASE_DIR=Path.cwd()

files=[f for f in BASE_DIR.iterdir() if f.is_file()]
for file in files:
    dossier_cible=EXTENSIONS_MAPPING.get(file.suffix,"Divers")
    dossier_cible_absolu= BASE_DIR / dossier_cible
    dossier_cible_absolu.mkdir(exist_ok=True)
    fichier_cible=dossier_cible_absolu / file.name
