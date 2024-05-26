import random
import math

def sinh_ngau_nhien_va_hien_thi():
    print("Dãy số ngẫu nhiên:")
    so_luong = random.randint(10, 20)  # Số lượng số nguyên trong dãy (từ 10 đến 20)
    day_so = [random.randint(1, 1000) for _ in range(so_luong)]
    print(day_so)
    return day_so

def kiem_tra_so_nguyen_to_chia_het_cho_7(day_so):
    print("Các số nguyên tố chia hết cho 7:")
    for so in day_so:
        if so % 7 == 0 and kiem_tra_so_nguyen_to(so):
            print(so)

def kiem_tra_so_nguyen_to(so):
    """
    Kiểm tra xem một số có phải là số nguyên tố hay không.
    """
    if so <= 1:
        return False
    if so <= 3:
        return True
    if so % 2 == 0 or so % 3 == 0:
        return False
    i = 5
    while i * i <= so:
        if so % i == 0 or so % (i + 2) == 0:
            return False
        i += 6
    return True

def tinh_tong_so_le(day_so):
    """
    Tính tổng các số lẻ trong dãy số.
    """
    tong = sum(so for so in day_so if so % 2 != 0)
    print("Tổng các số lẻ trong dãy số là:", tong)

def kiem_tra_so_chinh_phuong(day_so):
    print("Các số chính phương trong dãy số:")
    co_so_chinh_phuong = False
    for so in day_so:
        can_bac_hai = math.isqrt(so)
        if can_bac_hai * can_bac_hai == so:
            print(so)
            co_so_chinh_phuong = True
    if not co_so_chinh_phuong:
        print("Không có số chính phương trong dãy số.")
