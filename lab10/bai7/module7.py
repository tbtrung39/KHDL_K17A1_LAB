import random
import math

def sinh_day_so(n=100, max_value=1000):
    """
    Sinh ngẫu nhiên một dãy số gồm n số nguyên (tối đa 100 số).
    """
    if n > 100:
        n = 100
    return [random.randint(1, max_value) for _ in range(n)]

def hien_thi_day_so(day_so):
    """
    Hiển thị dãy số ra màn hình.
    """
    print("Dãy số đã sinh: ", day_so)

def so_chia_het_cho_7(day_so):
    """
    Liệt kê và hiển thị các số chia hết cho 7 trong dãy số.
    """
    ket_qua = [num for num in day_so if num % 7 == 0]
    print("Các số chia hết cho 7: ", ket_qua)
    return ket_qua

def tong_so_le(day_so):
    """
    Tính tổng các số lẻ trong dãy số.
    """
    tong = sum(num for num in day_so if num % 2 != 0)
    print("Tổng các số lẻ: ", tong)
    return tong

def so_chinh_phuong(day_so):
    """
    Kiểm tra và hiển thị các số chính phương trong dãy số.
    """
    chinh_phuong = [num for num in day_so if math.isqrt(num) ** 2 == num]
    if chinh_phuong:
        print("Các số chính phương: ", chinh_phuong)
    else:
        print("Không có số chính phương trong dãy.")
    return chinh_phuong
