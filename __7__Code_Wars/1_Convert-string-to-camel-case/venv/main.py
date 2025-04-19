def to_camel_case(text):
    splitText = text.replace("-", " ").replace("_", " ").split(" ")
    return "".join([splitText[i].title() if i != 0 else splitText[i] for i in range(len(splitText))])

if __name__ == "__main__":
    text = "The-stealth_Warrior"
    print(to_camel_case(text))