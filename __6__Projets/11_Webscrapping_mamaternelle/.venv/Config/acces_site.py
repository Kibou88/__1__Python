"""
acces_site
-----------
But: Permettre l'accès à un site web
-----------
Date de création: 2026-10-07
Date de modification: 2026-10-07
-----------
Version V1.0:
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm # bar de progression
from bs4 import BeautifulSoup
import time

from interface_acces_site import IHM

class Website_access:
    def __init__(self, url):
        if url.startswith('https://www.'):
            self.url = url
        else:
            print("L'url n'est pas valide")
            quit()

    def connexion(self):
        firefox_option=IHM().prepare_config()
        page = webdriver.Firefox(options=firefox_option)  #Création de l'objet page pour le navigateur Firefox
        #Ajouter options=firefox_option entre les () pour faire une connexion invisible
        page.get(self.url)
        page_source = page.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        with open("page.html", "w", encoding="utf-8") as f:
            f.write(str(soup))
        f.close()

    # A chercher balise <a class="post-thumbnail" et attribut href

if __name__ == '__main__':
    url = "https://www.mamaternelle.com/moyenne-section/lettres-moyenne-section"
    Website_access(url).connexion()
    # connexion()