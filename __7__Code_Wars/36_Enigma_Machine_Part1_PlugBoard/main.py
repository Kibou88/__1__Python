class Plugboard(object):
    def __init__(self, wires=""):
        for i in wires:
            if wires.count(i) > 1:
                raise Exception('A letter has more one connection')

        if 0 <= len(wires) <= 20 and len(wires) % 2 == 0:
            self.wires = wires
        else:
            raise Exception('Invalid wires')


    def process(self, c):
        """
        c: The single character to process
        """
        print(c)
        if not c in self.wires:
            return c
        index_letter = self.wires.index(c)
        if index_letter % 2 != 0:
            return self.wires[index_letter-1]
        else:
            return self.wires[index_letter+1]

if __name__ == "__main__":
    # enigma = Plugboard("ABCDEFGHIJKLMNOPQRSTUV")
    enigma2 = Plugboard()
    print(len("ABCDEFGHIJZYXWVUTSRQ"))
    print(enigma2.process("A"))
    print(enigma2.NUMBERS_WIRES)
    print(enigma2.process("B"))
    print(enigma2.NUMBERS_WIRES)
    print(enigma2.process("M"))
    print(enigma2.NUMBERS_WIRES)