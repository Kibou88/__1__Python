from pathlib import Path
import yt_dlp


def telecharger_audio(url: str, dossier_sortie: str = "musique") -> None:
    dossier = Path(dossier_sortie)
    dossier.mkdir(parents=True, exist_ok=True)

    options = {
        "format": "bestaudio/best",
        "outtmpl": str(dossier / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            informations = ydl.extract_info(url, download=True)
            titre = informations.get("title", "audio")
            print(f"Téléchargement terminé : {titre}.mp3")

    except yt_dlp.utils.DownloadError as erreur:
        print(f"Erreur de téléchargement : {erreur}")


if __name__ == "__main__":
    lien = input("URL de la vidéo YouTube : ").strip()

    if not lien:
        print("Aucune URL fournie.")
    else:
        telecharger_audio(lien)