def encode(st):
    dico_encode = {
        'a': "1",
        'e': "2",
        'i': "3",
        'o': "4",
        'u': "5",
    }
    for i in st:
        if i in dico_encode:
            st = st.replace(i, dico_encode[i])
    return st

def decode(st):
    dico_decode = {
        'a': "1",
        'e': "2",
        'i': "3",
        'o': "4",
        'u': "5",
    }
    for i in st:
        for key, value in dico_decode.items():
            if i == value:
                st = st.replace(i, key)
    return st


if __name__ == '__main__':
    to_encode = "Hello"
    to_decode = "H2ll4"

    print(encode(to_encode))
    print(decode(to_decode))