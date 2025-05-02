def spin_words(sentence):
    return " ".join([i[::-1] if len(i) >= 5 else i for i in sentence.split(" ")])

if __name__ == "__main__":
    sentence = "Hey fellow warriors"
    print(spin_words(sentence))