import random
import math

def sinh_ngau_nhien_day_so(max_so=100):
    """Sinh ngẫu nhiên một dãy số nguyên <= 100 số."""
    day_so = [random.randint(1, 100) for _ in range(random.randint(1, max_so))]
    print(f"Dãy số ngẫu nhiên: {day_so}")
    return day_so

def so_nguyen_to(n):
    """Kiểm tra một số có phải là số nguyên tố không."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def liet_ke_nguyen_to_chia_het_cho_7(day_so):
    """Liệt kê các số nguyên tố chia hết cho 7 trong dãy số."""
    ket_qua = [so for so in day_so if so_nguyen_to(so) and so % 7 == 0]
    print(f"Các số nguyên tố chia hết cho 7: {ket_qua}")
    return ket_qua

def tinh_tong_so_le(day_so):
    """Tính tổng các số lẻ thuộc dãy số."""
    tong = sum(so for so in day_so if so % 2 != 0)
    print(f"Tổng các số lẻ trong dãy: {tong}")
    return tong

def la_so_chinh_phuong(n):
    """Kiểm tra một số có phải là số chính phương không."""
    can_bac_hai = int(math.sqrt(n))
    return can_bac_hai * can_bac_hai == n

def kiem_tra_so_chinh_phuong(day_so):
    """Kiểm tra trong dãy có các số chính phương không và hiển thị chúng."""
    so_chinh_phuong = [so for so in day_so if la_so_chinh_phuong(so)]
    if so_chinh_phuong:
        print(f"Các số chính phương trong dãy: {so_chinh_phuong}")
    else:
        print("Không có số chính phương trong dãy.")
    return so_chinh_phuong