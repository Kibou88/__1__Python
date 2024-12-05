# Day 3 Advent of Code 2024
#----------------------------
import re
input_data = "./datas/3.txt"
new_datas = ""
pattern_be_deleted = r"[d][o][n]['][t][(][)].*?[d][o][(][)]"

pattern_regex = r"[m][u][l][(][0-9]{1,3}[,][0-9]{1,3}[)]"

with open(input_data, "r") as f:
    datas = f.read()

matches_wrong = re.findall(pattern_be_deleted, datas)

new_datas = re.sub(pattern_be_deleted, "", datas)

with open("./datas/test_datas.txt", "w+") as f:
    f.write(new_datas)


matches = re.findall(pattern_regex, new_datas)
print(len(matches))
total_number = 0

for match in matches:
    match = match[4:-1]
    numbers = match.split(",")
    print(numbers)
    total_number += (int(numbers[0]) * int(numbers[1]))

print(total_number)