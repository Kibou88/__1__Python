"""
Exercice 1 :
Crée un logger basique affichant en console le message "Démarrage programme" au niveau INFO et un message d’erreur
simulée au niveau ERROR. Configure un format date-niveau-message clair.
"""
import logging

logging.basicConfig(handlers=[logging.StreamHandler()],
                          level=logging.INFO,
                          format='%(asctime)s - %(levelname)s - %(message)s',
                          encoding='utf-8'
                          )
logging.info("Démarrage programme")
logging.error("Le programme n'as pas démarré")