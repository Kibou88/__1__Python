import re

def is_a_valid_message(message):
    if message == "":
        return True
    elif not message[0].isnumeric() or not message[-1].isalpha():
        return False
    else:
        matches = re.finditer(r'((\d+)(\D+))', message)
        for match in matches:
            if int(match.groups()[1]) != len(match.groups()[2]):
                return False
    return True


if __name__ in "__main__":
    message = "4code13hellocodewars"
    print(is_a_valid_message(message))