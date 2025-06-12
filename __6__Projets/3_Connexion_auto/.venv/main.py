# main.py
# ------------------------------------------------------------------
# But:
# Contient la logique du programme
# ------------------------------------------------------------------
# Date de création: 2025-06-03
# Date de modification: 2025-06-11
# ------------------------------------------------------------------
# Version: V1.0
import os

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import json

from notification import send_notification

FICHIER_JSON = ".\\datas\\data.json"

if os.path.exists(FICHIER_JSON):
    with open(FICHIER_JSON,"r") as f:
        data = json.load(f)
else:
    print("Le fichier de configuration est manquant")
    time.sleep(3)
    exit(1)

# Spécifiez le User-Agent que vous souhaitez utiliser
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
# Configuration pour le mode headless (invisble)
firefox_option = webdriver.FirefoxOptions()
firefox_option.add_argument('--headless')  # Active le mode headless
firefox_option.add_argument(f"user-agent={user_agent}")

page = webdriver.Firefox(options = firefox_option)

test = requests.get(data["url"])
if test.status_code != 200:
    print("Impossible de se connecter au site")
    time.sleep(3)
    exit(1)
else:

    # Accéder à la page web
    page.get(data["url"])

    # Remplir le formulaire
    case_first_name = page.find_element(By.ID, "first_name")
    case_first_name.send_keys(data["first_name"])

    case_last_name = page.find_element(By.ID, "last_name")
    case_last_name.send_keys(data["last_name"])

    case_sponsor_mail = page.find_element(By.ID, "sponsor_mail")
    case_sponsor_mail.send_keys(data["sponsor_mail"])

    # Sélectionner la durée
    duration_element = page.find_element(By.ID, "time")
    Select(duration_element).select_by_value(data["time_value"])

    # Cocher la case
    checkbox = page.find_element(By.ID, "read_checkbox")
    checkbox.click()

    # Soumettre le formulaire
    submit_form = page.find_element(By.ID, "submit_btn")
    submit_form.click()

    send_notification("Etat de la demande", "Demande a valider", "Connexion auto")

    """
    if test de connexion:
        page.quit() # Ferme la page
    else:
        print("Connexion mannuelle")
    """

