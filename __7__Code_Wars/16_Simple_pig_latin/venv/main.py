def pig_it(text):
    # split_text = text.split(" ")
    # new_word = []
    # for word in split_text:
    #     new_word.append(word[1:]+word[0]+"ay")
    # new_word = [(word[1:]+word[0]+"ay") for word in text.split(" ")]
    return " ".join([(word[1:] + word[0] + "ay") if word.isalpha() else word for word in text.split(" ")])

if __name__ == "__main__":
    text = "Pig latin is cool ?"
    check_text = "igPay atinlay siay oolcay ?"
    print(pig_it(text))
    print(pig_it(text) == check_text)