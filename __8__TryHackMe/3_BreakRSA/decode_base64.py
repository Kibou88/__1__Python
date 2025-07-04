import base64
import struct


def decode_ssh_rsa_key(ssh_key_b64):
    """
    Décode une clé SSH RSA et extrait le paramètre n (modulus)

    Args:
        ssh_key_b64 (str): La clé SSH en base64

    Returns:
        tuple: (n_bytes, n_decimal) où n_bytes sont les bytes et n_decimal la valeur décimale
    """

    # Décoder la base64
    key_bytes = base64.b64decode(ssh_key_b64)

    print(f"Taille totale des données décodées: {len(key_bytes)} bytes")

    # Parser le format SSH
    offset = 0

    # Fonction helper pour lire une string avec préfixe de longueur
    def read_string(data, offset):
        # Lire la longueur (4 bytes, big-endian)
        length = struct.unpack('>I', data[offset:offset + 4])[0]
        offset += 4
        # Lire les données
        string_data = data[offset:offset + length]
        offset += length
        return string_data, offset

    # Lire le type de clé (devrait être "ssh-rsa")
    key_type, offset = read_string(key_bytes, offset)
    print(f"Type de clé: {key_type.decode('utf-8')}")
    print(f"Nouveau offset: {offset}")

    # Lire l'exposant public (e)
    e_bytes, offset = read_string(key_bytes, offset)
    e_decimal = int.from_bytes(e_bytes, byteorder='big')
    print(f"Exposant public (e): {e_decimal}")
    print(f"Exposant public (e) en hex: {e_bytes.hex()}")
    print(f"Nouveau offset: {offset}")

    # Lire le modulus (n)
    n_bytes, offset = read_string(key_bytes, offset)
    n_decimal = int.from_bytes(n_bytes, byteorder='big')

    print(f"Modulus (n) - Taille: {len(n_bytes)} bytes")
    print(f"Modulus (n) en hex: {n_bytes.hex()}")
    print(f"Modulus (n) en décimal: {n_decimal}")
    print(f"Nouveau offset: {offset}")

    return n_bytes, n_decimal


# Votre clé SSH
ssh_key = "AAAAB3NzaC1yc2EAAAADAQABAAACAQDrZh8oe8Q8j6kt26IZ906kZ7XyJ3sFCVczs1Gqe8w7ZgU+XGL2vpSD100andPQMwDi3wMX98EvEUbTtcoM4p863C3h23iUOpmZ3Mw8z51b9DEXjPLunPnwAYxhIxdP7czKlfgUCe2n49QHuTqtGE/Gs+avjPcPrZc3VrGAuhFM4P+e4CCbd9NzMtBXrO5HoSV6PEw7NSR7sWDcAQ47cd287U8h9hIf9Paj6hXJ8oters0CkgfbuG99SVVykoVkMfiRXIpu+Ir8Fu1103Nt/cv5nJX5h/KpdQ8iXVopmQNFzNFJjU2De9lohLlUZpM81fP1cDwwGF3X52FzgZ7Y67Je56Rz/fc8JMhqqR+N5P5IyBcSJlfyCSGTfDf+DNiioRGcPFIwH+8cIv9XUe9QFKo9tVI8ElE6U80sXxUYvSg5CPcggKJy68DET2TSxO/AGczxBjSft/BHQ+vwcbGtEnWgvZqyZ49usMAfgz0t6qFp4g1hKFCutdMMvPoHb1xGw9b1FhbLEw6j9s7lMrobaRu5eRiAcIrJtv+5hqX6r6loOXpd0Ip1hH/Ykle2fFfiUfNWCcFfre2AIQ1px9pL0tg8x1NHd55edAdNY3mbk3I66nthA5a0FrKrnEgDXLVLJKPEUMwY8JhAOizdOCpb2swPwvpzO32OjjNus7tKSRe87w=="

# Décoder la clé
n_bytes, n_decimal = decode_ssh_rsa_key(ssh_key)

# print("\n" + "=" * 50)
# print("RÉSULTATS:")
# print("=" * 50)
# print(f"Bytes du modulus (n): {n_bytes}")
# print(f"Taille: {len(n_bytes)} bytes")
# print(f"Valeur décimale du modulus (n): {n_decimal}")

# Vérification de la taille en bits
import math

n_bits = math.ceil(math.log2(n_decimal)) if n_decimal > 0 else 0
print(f"Taille en bits: {n_bits} bits")