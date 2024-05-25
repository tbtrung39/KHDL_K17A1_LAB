import random
import math

def tao_day_so_ngau_nhien(do_dai):
    return [random.randint(1, 100) for _ in range(do_dai)]

def hien_thi_day_so(day_so):
    print("Dãy số ngẫu nhiên:")
    print(day_so)

def tim_so_nguyen_to_chia_het_cho_7(day_so):
    so_nguyen_to_chia_het_cho_7 = [num for num in day_so if num % 7 == 0 and la_so_nguyen_to(num)]
    if so_nguyen_to_chia_het_cho_7:
        print("Các số nguyên tố chia hết cho 7 trong dãy:")
        print(so_nguyen_to_chia_het_cho_7)
    else:
        print("Không có số nguyên tố chia hết cho 7 trong dãy.")

def tinh_tong_so_le(day_so):
    tong_so_le = sum(num for num in day_so if num % 2 != 0)
    print("Tổng các số lẻ trong dãy:", tong_so_le)

def kiem_tra_so_chinh_phuong(day_so):
    so_chinh_phuong = [num for num in day_so if math.isqrt(num) ** 2 == num]
    if so_chinh_phuong:
        print("Các số chính phương trong dãy:")
        print(so_chinh_phuong)
    else:
        print("Không có số chính phương trong dãy.")

def la_so_nguyen_to(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True