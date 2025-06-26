def number_of_carries(a, b):
    number_carries = 0
    result = a + b
    if len(str(a)) > len(str(b)):
        b = str(b).zfill(len(str(a)))
    elif len(str(a)) < len(str(b)):
        a = str(a).zfill(len(str(b)))

    if len(str(result)) > len(str(a)):
        result = str(result)[1:]
        for i in range(len(str(a))):
            if str(a)[i] == str(b)[i] == "0":
                continue
            if str(a)[i] >= str(result)[i] and str(b)[i] >= str(result)[i]:
                print(str(a)[i], str(b)[i], result[i])
                number_carries += 1
    else:
        for i in range(len(str(a))):
            if str(a)[i] == str(b)[i] == "0":
                continue
            if str(a)[i] >= str(result)[i] and str(b)[i] >= str(result)[i]:
                number_carries += 1
    return number_carries

if __name__ == '__main__':
    # number_of_carries(2, 9)
    # number_of_carries(9999,1)
    number_of_carries(3453700,9804970)