"""
SOLUTION DE MISTRAL AI
"""
def valid_braces(string):
    brace_pairs = {')': '(', '}': '{', ']': '['}
    stack = []
    if not len(string) % 2 == 0:
        # print("chaine impair")
        return False

    for character in string:
        if character in brace_pairs.values():
            stack.append(character)
        elif character in brace_pairs:
            if stack == [] or stack.pop() != brace_pairs[character]:
                return False
    return stack == []

if __name__ == "__main__":
    test = ["()", "(}","[]", "([{}])", "(((({{", "[(])", "(((({"]
    #      True, False, True, True, False, False, False
    for i in test:
        print(valid_braces(i))