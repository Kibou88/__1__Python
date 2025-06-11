"""
FORFAIT CAR PROBLEME DE TIMEOUT NON RESOLUS
"""
def duplicate_or_unique(inList):
    b = set(inList)
    return sum(inList) - sum(b) if len(inList) - len(b) == 1 else 2 * sum(b) - sum(inList)
if __name__ == "__main__":
    inList = [1,2,3,6,5,4,1]
    inList2 = [1,2,3,1,2,3,4]

    print(duplicate_or_unique(inList))
    print()
    print(duplicate_or_unique(inList2))