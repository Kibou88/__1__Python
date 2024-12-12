# Day 12 Advent of Code 2024
#----------------------------

FILE_TEST = "./datas/datas_test_12.txt"
FILE_PUZZLE = "./datas/12.txt"

def find_plot(datas):
    list_plot = []
    for y in range(len(datas)):
        for x in range(len(datas[y])):
            if datas[y][x] not in list_plot:
                list_plot.append(datas[y][x])
    return list_plot

def perimeter(datas, plot):
    perimeter_count = 0
    for y in range(len(datas)):
        for x in range(len(datas[y])):
            if datas[y][x] == plot:
                if y == 0 and x == 0:
                    if datas[y+1][x] == plot and datas[y][x+1] == plot:
                        perimeter_count += 2
                    if datas[y+1][x] != plot:
                        perimeter_count += 3
                    if datas[y][x+1] !=plot:
                        perimeter_count += 3
                    if datas[y+1][x] != plot and datas[y][x+1] != plot:
                        perimeter_count += 4
                    print(f"plot {plot}, perimetre {perimeter_count}")

                elif y == len(datas) and x == len(datas[y]):
                    if datas[y-1][x] == plot and datas[y][x-1] == plot:
                        perimeter_count += 2
                    if datas[y-1][x] != plot:
                        perimeter_count += 3
                    if datas[y][x-1] !=plot:
                        perimeter_count += 3
                    if datas[y-1][x] != plot and datas[y][x-1] != plot:
                        perimeter_count += 4

                elif y == 0 and x == len(datas[y]):
                    if datas[y+1][x] == plot and datas[y][x-1] == plot:
                        perimeter_count += 2
                    if datas[y+1][x] != plot:
                        perimeter_count += 3
                    if datas[y][x+1] != plot:
                        perimeter_count += 3
                    if datas[y+1][x] != plot and datas[y][x+1] != plot:
                        perimeter_count += 4
                    print(f"plot {plot}, perimetre {perimeter_count}")

                elif y == len(datas) and x == len(datas[y]):
                    if datas[y-1][x] == plot and datas[y][x-1] == plot:
                        perimeter_count += 2
                    if datas[y-1][x] != plot:
                        perimeter_count += 3
                    if datas[y][x-1] !=plot:
                        perimeter_count += 3
                    if datas[y-1][x] != plot and datas[y][x-1] != plot:
                        perimeter_count += 4


                else:
                    perimeter_count += 4

    return perimeter_count

if __name__ == '__main__':
    with open(FILE_TEST, 'r') as f:
        datas = f.read().splitlines()
    list_price_fence = []
    list_plot = find_plot(datas)

    for plot in list_plot:
        plot_count = list_plot.count(plot)
        print(f"plot {plot}: {perimeter(datas, plot)}")
