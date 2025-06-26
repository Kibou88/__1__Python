import random
import string
import itertools

def decode_xored(hex_encoded):
    bin_encoded = bytes.fromhex(hex_encoded)

    ascii_letter_digit = string.ascii_letters +string.digits

    bin_key = "ppYts".encode()

    # for alphadigit in itertools.product(ascii_letter_digit, repeat=5): #Pour une clé de 5 caractères alphanum
    #     key = ''.join(alphadigit)
    #     bin_key = ''.join(key).encode() # Convertir la chaine alphanumérique en bin
    #     for j in range(5): # 4 premiers caractères de la chaine encodée
    #         """
    #         bin_encoded[j]^bin_key[j] ==> (int) numéro décimal ASCII du caractère
    #         chr(int) ==> le caractère ASCII associé
    #         """
    #         decoded_start = "".join(chr(bin_encoded[j]^bin_key[j]))
    #     if("THM{" == decoded_start):
    #         return key
    for j in range(0, len(bin_key)):
        decoded_start = chr(bin_encoded[j] ^ bin_key[j])
    return decoded_start




def encode_xored(message):
    pass

if __name__ == '__main__':
    hex_encoded = "2438141112411135041635082d2b1604443a0101311e2b59031c3c2002370204205a17020816181f"
    print(decode_xored(hex_encoded))


    # print(len(hex_encoded))
    # bin_encoded = bytes.fromhex(hex_encoded)
    # bin_key = "abcgf".encode()
    # print(bin_encoded)
    # print(bin_key)
    # liste_test = []
    # for j in range(5):  # 4 premiers caractères de la chaine encodée
    #     liste_test.append(chr(bin_encoded[j] ^ bin_key[j]))
    # print(liste_test)