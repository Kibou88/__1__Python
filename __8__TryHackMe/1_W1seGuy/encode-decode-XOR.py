# encode-decode-XOR.py
# --------------------------------------------------------------------------------
# But:
# Encoder/Décoder une chaine XORé
# --------------------------------------------------------------------------------
# Date de création: 2025-06-27
# Date de modification: 2025-06-27
# --------------------------------------------------------------------------------
# Version V1
import binascii
from string import digits, ascii_letters


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
    def __init__(self, _message, _length_key=0, _key=None):
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
        """
        self.HMI()
        if (self.know_start != "" and self.know_end != ""):
            num_iterations_start = min(len(self.encrypted_bytes), len(self.know_start))
            self.key_start = "".join([chr(self.encrypted_bytes[i]^ord(self.know_start[i])) \
                                      for i in range(num_iterations_start)])
            num_iterations_end = min(len(self.encrypted_bytes), len(self.know_end))
            self.key_end = "".join([chr(self.encrypted_bytes[-num_iterations_end+i] ^ ord(end_test[i])) \
                                    for i in range(num_iterations_end)])

        else:
            pass

    def decode_message(self):
        """
        Permet de décoder un message XOR avec la clé trouvée
        :return:
        """

        if (self.key_start != "" and self.key_end != ""):
            self._key = self.key_start + self.key_end
            decoded = "".join([chr(self.encrypted_bytes[i] ^ ord(self._key[i % len(self._key)]))\
                               for i in range(len(self.encrypted_bytes))])
            if decoded.startswith(self.know_start) and decoded.endswith(self.know_end):
                print(f"La cle est: {self._key} et le message: {decoded}")
            else:
                print(f"Il y a eu une erreur")

    def HMI(self):
        """
        Affiche et permet de faire des choix à l'utilisateur
        :return:
        """
        if (self._key == None):
            print("Si vous connaissez une partie du message decrypte, pour:")
            print("\tLe debut, ecrire: start\n"
                  "\tLa fin, ecrire: end\n"
                  "\tLes deux, ecrire: both\n"
                  "\tSinon, ecrire: nothing\n")
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
    # encrypted_bytes = binascii.unhexlify(encoded_message)
    # num_iteration = min(len(encrypted_bytes), len(end_test))
    # print(encrypted_bytes[-2:])
    # print(chr(encrypted_bytes[-1] ^ ord(end_test[0])))
    test_to_decode = Decode_Message(encoded_message)
    test_to_decode.decode_key()
    test_to_decode.decode_message()
