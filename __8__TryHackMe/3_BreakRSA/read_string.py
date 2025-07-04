import base64
import struct


def read_string_explained(data, offset):
    """
    Fonction pour lire une "string" dans le format SSH avec explications détaillées

    Le format SSH utilise un système de "longueur + données" :
    - 4 bytes pour indiquer la longueur des données qui suivent
    - N bytes de données (où N est la longueur lue précédemment)
    """

    print(f"\n--- Lecture à partir de l'offset {offset} ---")

    # Étape 1: Lire les 4 premiers bytes qui contiennent la longueur
    length_bytes = data[offset:offset + 4]
    print(f"Bytes de longueur (4 bytes): {length_bytes.hex()}")

    # Étape 2: Décoder cette longueur en entier (big-endian, unsigned int)
    # '>' signifie big-endian (byte le plus significatif en premier)
    # 'I' signifie unsigned int (4 bytes)
    length = struct.unpack('>I', length_bytes)[0]
    print(f"Longueur décodée: {length} bytes")

    # Étape 3: Avancer l'offset de 4 bytes (on a lu la longueur)
    offset += 4
    print(f"Nouvel offset après lecture de la longueur: {offset}")

    # Étape 4: Lire les données réelles (N bytes où N = length)
    string_data = data[offset:offset + length]
    print(f"Données lues ({length} bytes): {string_data.hex()}")

    # Étape 5: Avancer l'offset du nombre de bytes lus
    offset += length
    print(f"Offset final après lecture des données: {offset}")

    return string_data, offset


# Exemple concret avec une clé SSH
ssh_key = "AAAAB3NzaC1yc2EAAAADAQABAAACAQDrZh8oe8Q8j6kt26IZ906kZ7XyJ3sFCVczs1Gqe8w7ZgU+XGL2vpSD100andPQMwDi3wMX98EvEUbTtcoM4p863C3h23iUOpmZ3Mw8z51b9DEXjPLunPnwAYxhIxdP7czKlfgUCe2n49QHuTqtGE/Gs+avjPcPrZc3VrGAuhFM4P+e4CCbd9NzMtBXrO5HoSV6PEw7NSR7sWDcAQ47cd287U8h9hIf9Paj6hXJ8oters0CkgfbuG99SVVykoVkMfiRXIpu+Ir8Fu1103Nt/cv5nJX5h/KpdQ8iXVopmQNFzNFJjU2De9lohLlUZpM81fP1cDwwGF3X52FzgZ7Y67Je56Rz/fc8JMhqqR+N5P5IyBcSJlfyCSGTfDf+DNiioRGcPFIwH+8cIv9XUe9QFKo9tVI8ElE6U80sXxUYvSg5CPcggKJy68DET2TSxO/AGczxBjSft/BHQ+vwcbGtEnWgvZqyZ49usMAfgz0t6qFp4g1hKFCutdMMvPoHb1xGw9b1FhbLEw6j9s7lMrobaRu5eRiAcIrJtv+5hqX6r6loOXpd0Ip1hH/Ykle2fFfiUfNWCcFfre2AIQ1px9pL0tg8x1NHd55edAdNY3mbk3I66nthA5a0FrKrnEgDXLVLJKPEUMwY8JhAOizdOCpb2swPwvpzO32OjjNus7tKSRe87w=="

# Décoder la base64
key_bytes = base64.b64decode(ssh_key)
print("bytes: ", key_bytes)

print("=" * 60)
print("ANALYSE DU FORMAT SSH - STRUCTURE DES DONNÉES")
print("=" * 60)

print(f"Taille totale des données: {len(key_bytes)} bytes")
print(f"Premières 20 bytes en hex: {key_bytes[:20].hex()}")

# Visualiser la structure complète
print("\n" + "=" * 60)
print("STRUCTURE COMPLÈTE DU FORMAT SSH RSA:")
print("=" * 60)
print("┌─────────────────────────────────────────────────────────┐")
print("│ Format SSH RSA:                                         │")
print("│ [4 bytes longueur][N bytes type] -> 'ssh-rsa'           │")
print("│ [4 bytes longueur][M bytes expo] -> exposant public (e) │")
print("│ [4 bytes longueur][K bytes modu] -> modulus (n)         │")
print("└─────────────────────────────────────────────────────────┘")

offset = 0

# Lire le type de clé
print("\n🔍 LECTURE DU TYPE DE CLÉ:")
key_type, offset = read_string_explained(key_bytes, offset)
print(f"Type de clé: '{key_type.decode('utf-8')}'")

# Lire l'exposant public
print("\n🔍 LECTURE DE L'EXPOSANT PUBLIC (e):")
e_bytes, offset = read_string_explained(key_bytes, offset)
e_decimal = int.from_bytes(e_bytes, byteorder='big')
print(f"Exposant public (e) en décimal: {e_decimal}")

# Lire le modulus
print("\n🔍 LECTURE DU MODULUS (n):")
n_bytes, offset = read_string_explained(key_bytes, offset)
n_decimal = int.from_bytes(n_bytes, byteorder='big')
print(f"Modulus (n) - Taille: {len(n_bytes)} bytes")
print(f"Modulus (n) - Premiers 20 bytes: {n_bytes[:20].hex()}")

print("\n" + "=" * 60)
print("EXPLICATION DU FORMAT struct.unpack('>I', ...)")
print("=" * 60)
print("struct.unpack('>I', data[offset:offset+4])[0]")
print("               ││")
print("               │└─ 'I' = unsigned int (4 bytes)")
print("               └─── '>' = big-endian (byte le plus significatif en premier)")
print()
print("Exemples de valeurs:")
print("- Bytes: 00 00 00 07 -> Longueur: 7")
print("- Bytes: 00 00 01 00 -> Longueur: 256")
print("- Bytes: 00 00 02 01 -> Longueur: 513")
print()
print("Big-endian signifie que le byte le plus significatif est en premier:")
print("00 00 01 00 = 0*256³ + 0*256² + 1*256¹ + 0*256⁰ = 256")