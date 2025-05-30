# AIDER PAR MISTRAL AI
def solution(args):
    result = []
    start_range = args[0]
    prev_num = args[0]

    for num in args[1:]:
        if num == prev_num + 1:
            prev_num = num
        else:
            if prev_num - start_range >= 2:
                result.append(f"{start_range}-{prev_num}")
            else:
                result.append(str(start_range))
                if prev_num != start_range:
                    result.append(str(prev_num))
            start_range = num
            prev_num = num

    if prev_num - start_range >= 2:
        result.append(f"{start_range}-{prev_num}")
    else:
        result.append(str(start_range))
        if prev_num != start_range:
            result.append(str(prev_num))

    return ",".join(result)

if __name__ == "__main__":
    test = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
    # solution(test)
    print(solution(test))