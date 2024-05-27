import random

def sinh_day_so():
    danh_sach_so = [random.randint(1, 100) for _ in range(100)]
    print("Dãy số ngẫu nhiên là:", danh_sach_so)
    return danh_sach_so

def liet_ke_so_nguyen_to_chia_het_cho_7(danh_sach):
    so_nguyen_to_chia_het_cho_7 = [so for so in danh_sach if so % 7 == 0 and is_prime(so)]
    print("Các số nguyên tố chia hết cho 7 trong dãy là:", so_nguyen_to_chia_het_cho_7)

def tinh_tong_so_le(danh_sach):
    tong_so_le = sum([so for so in danh_sach if so % 2 != 0])
    print("Tổng các số lẻ trong dãy là:", tong_so_le)

def kiem_tra_so_chinh_phuong(danh_sach):
    so_chinh_phuong = [so for so in danh_sach if is_perfect_square(so)]
    if so_chinh_phuong:
        print("Các số chính phương trong dãy là:", so_chinh_phuong)
    else:
        print("Không có số chính phương trong dãy.")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

