from string import ascii_lowercase

def keyword_cipher(msg, keyword):
    encryption_key  = []
    letter_lower_case = []
    for key_letter in keyword:
        if not key_letter in encryption_key:
            encryption_key.append(key_letter)
    for ascii_letter in ascii_lowercase:
        if not ascii_letter in encryption_key:
            encryption_key.append(ascii_letter)
        letter_lower_case.append(ascii_letter)

    return ''.join([encryption_key[letter_lower_case.index(letter)] if not letter == " " else letter \
                    for letter in msg.lower()] )


if __name__ == '__main__':
    msg = "Welcome home"
    keyword = "secret"

    print(keyword_cipher(msg, keyword))