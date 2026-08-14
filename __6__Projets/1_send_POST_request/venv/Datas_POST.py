# Datas_POST
# But:
# Contient la classe permettant de gérer les données de la requête POST
# ------------------------------------------------------------------------------------
# Date de création: 2025-03-07
# Date de modification: 2025-03-07
# -------------------------------------------------------------------------
# Version: V1

class Post_request():
    """
    Générer un objet contenant les données pour la requête POST
    """
    def __init__(self):
        pass

    def user_data(self) -> str:
        """
        Demande à l'utilisateur de saisir une paire clé-valeur pour la data du POST request
        :return
        self.user_key (str): Variable contenant la clé
        self.user_value (str): Variable contenant la valeur
        """
        self.user_key = input("Quel est le nom de la cle de la donnee: ")
        self.user_value = input("Quel est la valeur de cette cle: ")
    def encapsulation_data(self) -> dict:
        """
        Données à envoyer dans la requête POST
        :return
        (dict): Dico contenant la paire clé-valeur
        """
        return {
            self.user_key: self.user_value
        }
    def encapsulation_headers(self):
        """
        En-têtes de la requête
        :return
        (dict): Dico contenant le headers de la requête POST
        """
        #
        return {
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
