from base64 import b64encode, b64decode


def to_base_64(string):
    string_encoded = str(b64encode(bytes(string, "ascii")))
    if "=" in string_encoded:
        index = string_encoded.index("=")
        return string_encoded[2:index]
    else:
        return string_encoded[2:-1]
    # return string_encoded

def from_base_64(string):
    if len(string) % 4 != 0:
        string = string + ("="*(len(string) % 4))
    string_decoded = str(b64decode(bytes(string, "ascii")))
    return string_decoded[2:-1]

if __name__ == '__main__':
    string_to_encode = "this is a string!!"
    string_to_encode2 = "this is a test!"
    string_to_decode = "dGhpcyBpcyBhIHN0cmluZyEh"

    print(to_base_64(string_to_encode))
    print(to_base_64(string_to_encode2))
    print(from_base_64(string_to_decode))


