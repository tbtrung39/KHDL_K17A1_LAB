import random
import math

def sinh_day_so_nguyen(n):
    """Sinh ngẫu nhiên một dãy số nguyên <= n và hiển thị ra màn hình."""
    random_numbers = [random.randint(1, 100) for _ in range(n)]
    print("Dãy số ngẫu nhiên:", random_numbers)
    return random_numbers

def liet_ke_so_nguyen_to_chia_het_7(numbers):
    """Liệt kê và hiển thị các số nguyên tố chia hết cho 7 trong dãy."""
    primes_divisible_by_7 = [num for num in numbers if num % 7 == 0 and is_prime(num)]
    if primes_divisible_by_7:
        print("Các số nguyên tố chia hết cho 7 trong dãy:", primes_divisible_by_7)
    else:
        print("Không có số nguyên tố chia hết cho 7 trong dãy.")

def tinh_tong_so_le(numbers):
    """Tính tổng các số lẻ trong dãy."""
    odd_numbers = [num for num in numbers if num % 2 != 0]
    odd_sum = sum(odd_numbers)
    print("Tổng các số lẻ trong dãy là:", odd_sum)
    return odd_sum

def kiem_tra_so_chinh_phuong(numbers):
    """Kiểm tra trong dãy có các số chính phương không."""
    perfect_squares = [num for num in numbers if math.isqrt(num) ** 2 == num]
    if perfect_squares:
        print("Các số chính phương trong dãy:", perfect_squares)
    else:
        print("Không có số chính phương trong dãy.")

def is_prime(num):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
