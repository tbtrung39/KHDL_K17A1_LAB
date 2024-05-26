import random 
import math

def sinh_day_so():
    return [random.randint(1, 1000) for _ in range(100)]

def hien_thi_day_so(day_so):
    print("Dãy số ngẫu nhiên:")
    print(day_so)

def kiem_tra_so_nguyen_to_chia_het_cho_7(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def hien_thi_so_nguyen_to_chia_het_cho_7(day_so):
    so_nguyen_to_chia_het_cho_7 = [x for x in day_so if x % 7 == 0 and kiem_tra_so_nguyen_to_chia_het_cho_7(x)]
    print("Các số nguyên tố chia hết cho 7 trong dãy:")
    print(so_nguyen_to_chia_het_cho_7)

def tinh_tong_so_le(day_so):
    tong = sum(x for x in day_so if x % 2 != 0)
    print("Tổng các số lẻ trong dãy là:", tong)

def kiem_tra_so_chinh_phuong(n):
    return math.isqrt(n)**2 == n

def hien_thi_so_chinh_phuong(day_so):
    so_chinh_phuong = [x for x in day_so if kiem_tra_so_chinh_phuong(x)]
    if so_chinh_phuong:
        print("Các số chính phương trong dãy là:", so_chinh_phuong)
    else:
        print("Không có số chính phương trong dãy.")