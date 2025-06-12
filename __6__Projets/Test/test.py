import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import json

fichier_json = "data.json"

with open(fichier_json,"r") as f:
    data = json.load(f)

url = "https://portal-lehaillan.scalian.com/auth/sponsor.html?url=1q6gPKCYnRMKnGybQ8twEMZcM4ihChOAFAqX0VNFsUtSXscl01P0FpFsK0i7rgDRZTOp201tvS0VUe0XB3JVpi40GgxD6Lk1AAn8No3e7KSYzQ4arUl+5luT4xL1WKs1u6EpSUK1N2db+PmQobtd/glKsVAc7s6KuR6kB8vOt5M="

# Spécifiez le User-Agent que vous souhaitez utiliser
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
# Configuration pour le mode headless (invisble)
firefox_option = webdriver.FirefoxOptions()
firefox_option.add_argument('--headless')  # Active le mode headless
firefox_option.add_argument(f"user-agent={user_agent}")

page = webdriver.Firefox(options = firefox_option)

test = requests.get(url)
if test.status_code != 200:
    print("end")
else:
    # Accéder à la page web
    page.get(url)

    # Remplir le formulaire
    case_first_name = page.find_element(By.ID, "first_name")
    case_first_name.send_keys(data["first_name"])

    case_last_name = page.find_element(By.ID, "last_name")
    case_last_name.send_keys(data["last_name"])

    case_sponsor_mail = page.find_element(By.ID, "sponsor_mail")
    case_sponsor_mail.send_keys(data["sponsor_mail"])

    # Sélectionner la durée
    duration_element = page.find_element(By.ID, "time")
    Select(duration_element).select_by_value("240")

    # Cocher la case
    checkbox = page.find_element(By.ID, "read_checkbox")
    checkbox.click()

    # Soumettre le formulaire
    submit_form = page.find_element(By.ID, "submit_btn")
    submit_form.click()

    """
    if test de connexion:
        page.quit() # Ferme la page
    else:
        print("Connexion mannuelle")
    """