# Day 22 Advent of Code 2024
#----------------------------
from functools import cache

@cache
def mix(a, b):
    # OK --> Bitwise XOR operation
    return a ^ b

@cache
def prune(number):
    # OK --> secret number modulo 16777216
    return number % 16777216

@cache
def multiply_64(number):
    # Multiply secret number by 64 and prune it
    return prune(mix(number * 64, number))

@cache
def divide_32(number):
    # Divide secret number by 32, mix it and prune it
    return prune(mix(int(number/32), number))

@cache
def multiply_2048(number):
    # Multiply secret number by 2048, mix it and prune it
    return prune(mix(number * 2048, number))

if __name__ == "__main__":
    secret_number = 1
    for i in range(2000):
        secret_number = multiply_2048(divide_32(multiply_64(secret_number)))
    print(secret_number)