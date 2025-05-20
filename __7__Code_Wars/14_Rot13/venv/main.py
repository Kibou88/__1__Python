def rot13(message):
    temp = []
    for character in message:
        if character.isalpha() and character.islower():
            if (ord(character) + 13) > 122:
                temp.append(chr(ord(character) + 13 - 122 + 96))
            else:
                temp.append(chr(ord(character) + 13))
        elif character.isalpha() and character.isupper():
            if (ord(character) + 13) > 90:
                temp.append(chr(ord(character) + 13 - 90 + 64))
            else:
                temp.append(chr(ord(character) + 13))
        else:
            temp.append(character)

    return "".join(temp)


if __name__ == "__main__":
    message = ["test", "Test", "Test2"]
    for i in message:
        print(rot13(i))
