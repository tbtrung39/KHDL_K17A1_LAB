import random

def rd_str(n, start=1, end=1000):
    return [random.randint(start, end) for _ in range(n)]

def list_7(n):
    return [num for num in n if num % 7 == 0]

def sum_odd(n):
    return sum(num for num in n if num % 2 != 0)