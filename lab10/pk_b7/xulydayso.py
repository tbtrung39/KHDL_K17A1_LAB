import random
import math

def sinh_ngau_nhien_day_so():
    """Sinh ngẫu nhiên một dãy số <= 100 số nguyên"""
    so_luong = random.randint(1, 100)
    day_so = [random.randint(0, 1000) for _ in range(so_luong)]
    return day_so

def la_so_nguyen_to(n):
    """Kiểm tra một số có phải là số nguyên tố hay không"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def liet_ke_nguyen_to_chia_het_cho_7(day_so):
    """Liệt kê các số nguyên tố chia hết cho 7 trong dãy số"""
    return [num for num in day_so if la_so_nguyen_to(num) and num % 7 == 0]

def tinh_tong_so_le(day_so):
    """Tính tổng các số lẻ trong dãy số"""
    return sum(num for num in day_so if num % 2 != 0)

def kiem_tra_va_hien_thi_so_chinh_phuong(day_so):
    """Kiểm tra và hiển thị các số chính phương trong dãy số"""
    so_chinh_phuong = [num for num in day_so if math.isqrt(num) ** 2 == num]
    return so_chinh_phuong if so_chinh_phuong else None
