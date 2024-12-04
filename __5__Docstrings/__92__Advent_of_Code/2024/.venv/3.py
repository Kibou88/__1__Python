# Day 3 Advent of Code 2024
#----------------------------
import re
input_data = "./datas/3.txt"
new_datas = ""
pattern_be_deleted = r"[d][o][n]['][t][(][)].{1,}[d][o][(][)]"

pattern_regex = r"[m][u][l][(][0-9]{1,3}[,][0-9]{1,3}[)]"

with open(input_data, "r") as f:
    datas = f.read()

nb_dont = datas.count("don't()")

for _ in range(nb_dont):
    try:
        index_dont = datas.index("don't()")
        index_do = datas.index("do()", index_dont)
        ligne = datas[index_dont:index_do]
        datas = datas.replace(ligne, "")
    except:
        break

with open("./datas/final.txt", 'w+') as f:
    f.write(datas)

with open("./datas/final.txt", 'r+') as f:
    new_datas = f.read()

matches = re.findall(pattern_regex, new_datas)

total_number = 0

for match in matches:
    match = match[4:-1]
    numbers = match.split(",")
    print(numbers)
    total_number += (int(numbers[0]) * int(numbers[1]))

print(total_number)