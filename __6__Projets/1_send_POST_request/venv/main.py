# send POST request
# But:
# Envoyer une requête POST avec des données et vérifier la bonne réception du serveur
# ------------------------------------------------------------------------------------
# Date de création: 2025-03-06
# Date de modification: 2025-03-06
# -------------------------------------------------------------------------
# Version: V1


import requests
import time

# URL de destination
url = "http://sandbox1.reply.it/web1-f1103cad4b0542c69e23b267e173799295c4f217/got-a-goat"

# Données à envoyer dans la requête POST
data = {
    "type": "blue"
}

# En-têtes de la requête
headers = {
    "Host": "sandbox1.reply.it",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Accept": "*/*",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "10",
    "Origin": "http://sandbox1.reply.it",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": "http://sandbox1.reply.it/web1-f1103cad4b0542c69e23b267e173799295c4f217/"
}

# Créer une session pour maintenir les cookies
session = requests.Session()

# Nombre de requêtes à envoyer
num_requests = 35

# Délai entre les requêtes (en secondes)
delay = 2

# Variable pour cumuler les points
total_points = 0

# Boucle pour envoyer les requêtes
while True:
    # Envoi de la requête POST
    response = session.post(url, data=data, headers=headers)

    # Vérification du statut de la réponse
    if response.status_code == 200:
        # Mise à jour des points cumulés
        response_data = response.json()
        print(f"Réponse du serveur : {response_data}")
        # Vérifier si le total_score atteint 65536
        if response_data['total_score'] == 65536:
            print("Total score atteint 65536 ! Sauvegarde de la page HTML...")
            # Obtenir le contenu HTML de la page
            html_response = session.get("http://sandbox1.reply.it/web1-f1103cad4b0542c69e23b267e173799295c4f217/")
            if html_response.status_code == 200:
                # Sauvegarder le contenu HTML dans un fichier
                with open("page_saved.html", "w", encoding="utf-8") as file:
                    file.write(html_response.text)
                print("Page HTML sauvegardée avec succès !")
            else:
                print(f"Erreur lors de la récupération de la page HTML. Code de statut : {html_response.status_code}")
            break  # Arrêter la boucle après avoir sauvegardé la page
    else:
        print(f"Erreur lors de la requête . Code de statut : {response.status_code}")
        print("Réponse du serveur :", response.text)
        break

    # Attente avant d'envoyer la prochaine requête
    time.sleep(delay)
