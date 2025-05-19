def int32_to_ip(int32):
    return f"{int(f'{int32:032b}'[0:8], 2)}.{int(f'{int32:032b}'[8:16], 2)}.{int(f'{int32:032b}'[16:24], 2)}" \
           f".{int(f'{int32:032b}'[24:32], 2)}"

if __name__ == "__main__":
    test = [2154959208, 0, 32]
    # Affiche la valeur 0 en binaire sur 32 bits
    print(f"{0:032b}")
    print(bin(2154959208)[10:18])
    for i in test:
        print(int32_to_ip(i))