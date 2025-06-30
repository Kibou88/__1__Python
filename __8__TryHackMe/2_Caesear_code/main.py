from string import ascii_uppercase
import random
all_combinations = 26
dict_decrypt = {}
def crypt_caesar(message):
    key_encrypt = random.randint(1,26)
    temp = []
    for j in range(len(message)):
        if ascii_uppercase.index(message[j]) + key_encrypt < len(ascii_uppercase):
            temp.append(ascii_uppercase[ascii_uppercase.index(message[j]) + key_encrypt])
        elif ascii_uppercase.index(message[j]) + key_encrypt >= len(message):
            temp.append(ascii_uppercase[ascii_uppercase.index(message[j]) + key_encrypt - len(ascii_uppercase)])
    return "".join(temp)


def decrypt_caesar(plaintext):
    for i in range(1, all_combinations):
        temp = []
        for j in range(len(plaintext)):
            if ascii_uppercase.index(plaintext[j])+i < len(ascii_uppercase):
                temp.append(ascii_uppercase[ascii_uppercase.index(plaintext[j])+i])
            elif ascii_uppercase.index(plaintext[j])+i >= len(plaintext):
                temp.append(ascii_uppercase[ascii_uppercase.index(plaintext[j])+i-len(ascii_uppercase)])
        dict_decrypt[i] = "".join(temp)
    return dict_decrypt


if __name__ == "__main__":
    plaintext = "ICANENCRYPT"
    message_crypted = "XRPCTCRGNEI"
    print(crypt_caesar(plaintext))
    print(decrypt_caesar(message_crypted))
