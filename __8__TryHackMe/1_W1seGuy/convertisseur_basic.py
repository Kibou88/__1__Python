# convertisseur_basic.py
# --------------------------------------------------------------------------------
# But:
# Transformer une chaine de type string, binaire ou hexadécimal par un autre type
# --------------------------------------------------------------------------------
# Date de création: 2025-06-26
# Date de modification: 2025-06-26
# --------------------------------------------------------------------------------
# Version V1

import binascii

class Convertisseur():
    """
    Permet de convertir un message en str, hexa ou binaire en fonction du choix utilisateur
    """
    def __init__(self, _message):
        self._message = _message

    def is_hex(self):
        """
        Test du format du message en hexa
        :return:
        True (bool) Si le message est hexa sinon renvoie False (bool)
        """
        hex_digits = set('0123456789abcdefABCDEF')
        if not isinstance(self._message, str) or not all(c in hex_digits for c in self._message):
            return False
        try:
            int(self._message, 16)
        except ValueError:
            return False
        return True

    def is_bin(self):
        """
        Test du format du message en binaire
        :return:
        True (bool) Si le message est hexa sinon renvoie False (bool)
        """
        binary_str = '10'
        for character in self._message:
            if character not in binary_str:
                return False
        return True

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

    def to_hex(self):
        """
        Convertit le message bin ou str en message hexa
        Si le message n'est pas dans un format connu levée d'un TypeError
        :return:
        message (hex) Message en hexa
        """
        if (self.is_bin()):
            self._message = (hex(int(self._message, 2)))[2:]
        elif (self.is_str()):
            # Sans decode(), output serait b'xxxxxxxx'
            # Avec decode(), output est xxxxxxxx
            self._message = binascii.hexlify(self._message.encode()).decode()
        else:
            raise TypeError("Le message n'est pas au format string!!")
        return self._message

    def to_bin(self):
        """
        Convertit le message hexa ou str en message bin
        Si le message n'est pas dans un format connu levée d'un TypeError
        :return:
        message (bin) Message en binaire
        """
        if (self.is_str()):
            # ord(letter) traduit la lettre à son numéro décimal dans la table ASCII
            # bin(ord(letter)) affiche le code binaire du numéro décimal dans la table ASCII (enlève 0 inutiles)
            self._message = "".join([("0" * (8 - len(bin(ord(letter))[2:])) + bin(ord(letter))[2:]) \
                                     for letter in self._message])
        elif (self.is_hex()):
            self._message = hex(int(self._message, 2))[2:]
        else:
            raise TypeError("Le message n'est pas aux formats string et hexa!")
        return self._message

    def to_str(self):
        """
        Convertit le message bin ou hexa en message str
        :return:
        message (str) Message en str
        """
        if (self.is_hex()):
            # Sans decode(), output serait b'xxxxxxxx'
            # Avec decode(), output est xxxxxxxx
            self._message = binascii.unhexlify(message_hexa).decode()
        elif (self.is_bin()):
            # Convertir la chaîne binaire en un entier
            int_value = int(self._message, 2)
            # Convertir l'entier en bytes et décoder en chaîne de caractères
            self._message = int_value.to_bytes((int_value.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
        else:
            raise TypeError("Le message n'est ni au format hexa et binaire!!")
        return self._message


if __name__ == '__main__':
    # ------------ Test str en bin et hexa ---------------
    message_str = "THM{"
    print("Message str: ", message_str)
    test1 = Convertisseur(message_str)
    test2 = Convertisseur(message_str)
    message_hexa = test1.to_hex() #output: 54484d7b
    message_bin = test2.to_bin() #output: 1010100010010000100110101111011
    print("Message convertit en hexa: ", message_hexa)
    print("Message convertit en bin: ", message_bin)
    print("\n")
    # ------------------------------------------------------

    # ------------ Test bin en str et hexa ---------------
    message_bin = "01010100010010000100110101111011"
    print("Message bin: ", message_bin)
    test3 = Convertisseur(message_bin)
    test4 = Convertisseur(message_bin)
    message_str = test3.to_str() #output: THM{
    message_hexa = test4.to_hex() #output: 54484d7b
    print("Message convertit en str: ", message_str)
    print("Message convertit en hexa: ", message_hexa)
    print("\n")
    # ------------------------------------------------------

    # ------------ Test hexa en str et bin ---------------
    message_hexa = "54484d7b"
    print("Message hexa: ", message_hexa)
    test5 = Convertisseur(message_hexa)
    test6 = Convertisseur(message_hexa)
    message_str = test5.to_str()  # output: 54484d7b
    message_bin = test6.to_bin()  # output: THM{
    print("Message convertit en str: ", message_str)
    print("Message convertit en bin: ", message_bin)
