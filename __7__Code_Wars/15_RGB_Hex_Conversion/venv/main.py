def rgb(r, g, b):
    if 0 <= r <= 15:
        hex_r = "0" + str(hex(r)[-1])
    elif 255 >= r >= 16:
        hex_r = f"{r:x}"
    elif r < 0:
        hex_r = "00"
    elif r > 255:
        hex_r = "FF"

    if 0 <= g <= 15:
        hex_g = "0" + str(hex(g)[-1])
    elif 255 >= g >= 16:
        hex_g = f"{g:x}"
    elif g < 0:
        hex_g = "00"
    elif g > 255:
        hex_g = "FF"

    if 0 <= b <= 15:
        hex_b = "0" + str(hex(b)[-1])
    elif 255 >= b >= 16:
        hex_b = f"{b:x}"
    elif b < 0:
        hex_b = "00"
    elif b > 255:
        hex_b = "FF"

    return hex_r.upper() + hex_g.upper() + hex_b.upper()

if __name__ == "__main__":

    colors = [[255, 255, 300], [148, 0, 211], [255, 255, 255], [-20, 275, 125]]
    # print("{:x}".format(255))
    # print(hex(1))
    print(f"{275:x}")
    for color in colors:
        print(rgb(color[0], color[1], color[2]))