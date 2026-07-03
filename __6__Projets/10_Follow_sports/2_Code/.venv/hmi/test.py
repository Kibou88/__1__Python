liste_test = ["3.5", "3,5", '4', "3.r", "4,r5",".4.r5"]

for i in liste_test:
    error_flag = False
    if "," in i:
        i = i.replace(",", ".")
    print(i)
    for caractere in i:
        if not caractere.isdigit() and not caractere == "." or not i.count(".") == 1:
            print(caractere)
            print("ERROR")
            error_flag = True
            break

    if not error_flag:

        print(i.isnumeric())
        print(i.isdecimal())
        print(i.isalpha())
        print(i.isdigit())
        print(float(i))
        print("---------------------")