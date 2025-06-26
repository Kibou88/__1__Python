import string
import random

res = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
key = res

def setup(key):
    flag = 'THM{thisisafakeflag}' #
    xored = ""

    for i in range(0,len(flag)):
        xored += chr(ord(flag[i]) ^ ord(key[i%len(key)]))

    print(xored)
    hex_encoded = xored.encode().hex()
    hex_decoded = hex_encoded.recv(4096).decode().strip()
    return hex_encoded, hex_decoded

if __name__ == '__main__':
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    key = res

    setup(key)