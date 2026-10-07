"""
interface_acces_site
-----------
But: Affiche les différents messages pour la configuration des paramètres pour accéder au site.
    Récupère la saisie utilisateur
-----------
Date de création: 2026-10-07
Date de modification: 2026-10-07
-----------
Version V1.0:
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

class IHM():

    def __init__(self):
        pass

    def user_agent(self):
        # Spécifiez le User-Agent que vous souhaitez utiliser
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:157.0) Gecko/20100101 Firefox/157.0"
        self.firefox_option.add_argument(f"user-agent={user_agent}")

    def invisible_mode(self):
        self.firefox_option.add_argument('--headless')  # Active le mode headless


    def prepare_config(self):
        # Configuration pour le mode headless (invisble)
        self.firefox_option = webdriver.FirefoxOptions()
        user_choice = input("Voulez-vous le mode fenêtre invisible (oui) ou fenêtre visible (non)? ")
        if user_choice.lower() in ["oui", "yes", "true"]:
            self.invisible_mode()
        self.user_agent()
        print("Configuration firefox prête")
        return self.firefox_option

if __name__ == '__main__':
    pass