import heapq
def solution(lst):
    # for x in range(len(lst) - 1):
    #     if lst[x] == lst[x+1]:

    inverse_number = [-x for x in lst]
    heapq.heapify(inverse_number) # Equivalent à sorted
    i = -heapq.heappop(inverse_number)
    j = -heapq.heappop(inverse_number)
    print(i, j)
    print(inverse_number)


if __name__ == "__main__":
    lst = [6, 9, 21]

    solution(lst)