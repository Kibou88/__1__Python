# send POST request
# But:
# Envoyer une requête POST avec des données et vérifier la bonne réception du serveur
# ------------------------------------------------------------------------------------
# Date de création: 2025-03-06
# Date de modification: 2025-03-06
# -------------------------------------------------------------------------
# Version: V2
# - Ajout de la classe Post_request (V2)
# - MAJ forme PEP8 (V2)

import requests
import time

from Datas_POST import Post_request

# URL de destination
URL = "http://sandbox1.reply.it/web1-f1103cad4b0542c69e23b267e173799295c4f217/got-a-goat"

# Créer une session pour maintenir les cookies
SESSION = requests.Session()

# Délai entre les requêtes (en secondes)
DELAY = 2

message_post = Post_request()
message_post.user_data()

# Boucle pour envoyer les requêtes
while True:
    # Envoi de la requête POST
    response = SESSION.post(URL, data=message_post.encapsulation_data(), headers=message_post.encapsulation_headers())

    # Vérification du statut de la réponse
    if response.status_code == 200:
        # Mise à jour des points cumulés
        response_data = response.json()
        print(f"Réponse du serveur : {response_data}")
        # Vérifier si le total_score atteint 65536
        if response_data['total_score'] == 65536:
            print("Total score atteint 65536 ! Sauvegarde de la page HTML...")
            # Obtenir le contenu HTML de la page
            html_response = SESSION.get("http://sandbox1.reply.it/web1-f1103cad4b0542c69e23b267e173799295c4f217/")
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
    time.sleep(DELAY)
