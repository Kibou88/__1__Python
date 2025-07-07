# encode-decode-XOR.py
# --------------------------------------------------------------------------------
# But:
# Encoder/Décoder une chaine XORé
# --------------------------------------------------------------------------------
# Date de création: 2025-06-27
# Date de modification: 2025-06-27
# --------------------------------------------------------------------------------
# Version V1.1:
# - Partie "début du message connu" ajoutée (V1.1)
# - Ajout de couleur (V1.1)
# - Ajustement de la méthode "decode_message" (V1.1)

import binascii
from string import digits, ascii_letters

from class_colors import *

class Encode_Message():
    def __init__(self, _message):
        self._message= _message

    def encode(self):
        pass

    def key(self):
        pass

class Decode_Message():
    """
    Permet de décoder un message XOR
    """
    def __init__(self, _message, _length_key=None, _key=None):
        self._message = _message
        self.encrypted_bytes = binascii.unhexlify(_message) # Conversion du message hexa en binaire
        self._length_key = _length_key
        self._key = _key
        self.key_start = ""

    def is_str(self):
        """
        Test du format du message en str
        :return:
        True (bool) Si le message est str sinon renvoie False (bool)
        """
        try:
            isinstance(self._message, str)
        except TypeError:
            return False
        return True

    def decode_key(self):
        """
        Permet de trouver la clé de cryptage
        :return:
        self._key (str): clé trouvée pour le message codée
        """
        # self.HMI_hexa_message()
        self.HMI_key()
        if (self.know_start != ""):
            key = []
            for index_bin in range(len(self.encrypted_bytes)):
                if index_bin >= len(self.know_start):
                    break
                for ascii_alphanum in ascii_letters:
                    if (chr(self.encrypted_bytes[index_bin] ^ ord(ascii_alphanum)) == self.know_start[index_bin]):
                        key.append(ascii_alphanum)
            self._key = "".join(key)

        elif (self.know_start != "" and self.know_end != ""):
            num_iterations_start = min(len(self.encrypted_bytes), len(self.know_start))
            self.key_start = "".join([chr(self.encrypted_bytes[i]^ord(self.know_start[i])) \
                                      for i in range(num_iterations_start)])
            num_iterations_end = min(len(self.encrypted_bytes), len(self.know_end))
            self.key_end = "".join([chr(self.encrypted_bytes[-num_iterations_end+i] ^ ord(end_test[i])) \
                                    for i in range(num_iterations_end)])
            self._key = self.key_start + self.key_end

        else:
            pass

    def decode_message(self):
        """
        Permet de décoder et d'afficher le message XOR avec la clé trouvée
        :return:
        """
        decoded = "".join([chr(self.encrypted_bytes[i] ^ ord(self._key[i % len(self._key)])) \
                           for i in range(len(self.encrypted_bytes))])
        if (self.know_start != ""):
            if decoded.startswith(self.know_start):
                print(f"La cle est: {Colors.YELLOW}{self._key}{Colors.END} et le message est: "
                      f"{Colors.YELLOW}{decoded}{Colors.END}")
        elif (self.key_start != "" and self.key_end != ""):
            if decoded.startswith(self.know_start) and decoded.endswith(self.know_end):
                print(f"La cle est: {Colors.YELLOW}{self._key}{Colors.END} et le message est: "
                      f"{Colors.YELLOW}{decoded}{Colors.END}")
        else:
            print(f"Il y a eu une erreur")

    def HMI_key(self):
        """
        Affiche et permet de faire des choix à l'utilisateur
        :return:
        self.know_start and/or self.know_end (str): Début et/ou fin du message décodé connu
        """
        if (self._key == None):
            print("Si vous connaissez une partie du message decrypte, pour:")
            print(f"\tLe debut, ecrire: {Colors.BLUE}{Colors.BOLD}start{Colors.END}\n"
                  f"\tLa fin, ecrire: {Colors.BLUE}{Colors.BOLD}end{Colors.END}\n"
                  f"\tLes deux, ecrire: {Colors.BLUE}{Colors.BOLD}both{Colors.END}\n"
                  f"\tSinon, ecrire: {Colors.BLUE}{Colors.BOLD}nothing{Colors.END}\n")

            key_parts_know = input("Quelle(s) partie(s) du message decrypte connaissez vous? ")
            if (key_parts_know.lower() == "start"):
                self.know_start = input("Ecrire le debut du message decrypte: ")
            elif (key_parts_know.lower() == "end"):
                self.know_end = input("Ecrire la fin du message decrypte: ")
            elif (key_parts_know.lower() == "both"):
                self.know_start = input("Ecrire le debut du message decrypte: ")
                self.know_end = input("Ecrire la fin du message decrypte: ")
            else:
                raise ValueError("Ce que vous avez ecrit n'est pas dans la liste")
        else:
            self._key = input("Ecrire la cle pour decrypte le message: ")


if __name__ == '__main__':
    test = "THM{"
    end_test = "}"
    encoded_message = "381c2401205d35051424292c1d3b2418600a11332d3a1b493100181012051e20104a251e2c26082d"
    XOR_message = ("1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373"
                   "1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60")


    test_to_decode = Decode_Message(XOR_message)
    test_to_decode.decode_key()
    test_to_decode.decode_message()
