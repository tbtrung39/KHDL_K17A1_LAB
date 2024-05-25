import random
import math

def day_so(n):
    return [random.randint(1, 100) for _ in range(n)]

def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_chia_het_7(day_so):
    return [n for n in day_so if kiem_tra_so_nguyen_to(n) and n % 7 == 0]

def tong_so_le(day_so):
    return sum(n for n in day_so if n % 2 != 0)

def kiem_tra_so_chinh_phuong(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def so_chinh_phuong_trong_day(day_so):
    return [n for n in day_so if kiem_tra_so_chinh_phuong(n)]
