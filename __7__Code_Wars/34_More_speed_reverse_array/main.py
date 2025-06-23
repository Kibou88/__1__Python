"""
AIDE PAR MISTRAL POUR LA PERFORMANCE
"""
def reverse(seq):
    length = len(seq)
    for i in range(length // 2):
        seq[i], seq[length - i - 1] = seq[length - i - 1], seq[i]
    #    a, b = b, a
    #  si a = 5, b = 2 ==> a = 2, b = 5

    return seq

if __name__ == '__main__':
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(reverse(seq))