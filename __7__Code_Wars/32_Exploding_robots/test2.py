commands = ["U", "D"]

def check_collision(x1, y1, x2, y2, index, memo=None):
    if memo is None:
        memo = {}

    if (x1, y1, x2, y2, index) in memo:
        return memo[(x1, y1, x2, y2, index)]

    if index == len(commands):
        return False

    memo[(x1, y1, x2, y2, index)] = check_collision(n-1, memo) + check_collision(n-2, memo)
    return memo[(x1, y1, x2, y2, index)]

print(fibonacci(10))

