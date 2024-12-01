# Day 1 Advent of Code 2024
#----------------------------

input_data = "/home/kibou/Bureau/Python/__1__Python/__5__Docstrings/__92__Advent_of_Code/2024/.venv/datas/1.txt"
left_column = []
right_column = []
total_sum = 0
total_multi = 0

with open(input_data, 'r') as f:
    lines = f.read().splitlines()

for line in range(len(lines)):
    left_column.append(lines[line][0:5])
    right_column.append(lines[line][-5:])

left_column.sort()
right_column.sort()

for i in range(len(right_column)):
    total_sum += abs(int(left_column[i]) - int(right_column[i]))
    total_multi += int(left_column[i]) * int(right_column.count(left_column[i]))

print(f"Total sum: {total_sum}")
print(f"Total multiplication: {total_multi}")