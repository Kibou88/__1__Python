def order(sentence):
  numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
  splitSentence = sentence.split(" ")
  return " ".join(splitSentence[i] for number in numbers for i in range(len(splitSentence))
                  if number in splitSentence[i])

if __name__ == "__main__":
    sentence = "4of Fo1r pe6ople g3ood th5e the2"
    print(order(sentence))