import random
import math

def tao_danh_sach():
    danh_sach_ngau_nhien = [] 
    so_luong = random.randint(1, 101)

    for i in range(so_luong):
        danh_sach_ngau_nhien.append(random.randint(1, 101))

    return danh_sach_ngau_nhien

def chia_het7(tao_danh_sach):
    so_nguyen_to_chia_het7 = []

    for num in tao_danh_sach:
        if num % 7 == 0 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            so_nguyen_to_chia_het7.append(num)

    return so_nguyen_to_chia_het7

def tong(tao_danh_sach):
    t = 0

    for num in tao_danh_sach:
        if num % 21 == 0:
            t += num

    return t

def kiem_tra_so_chinh_phuong(tao_danh_sach):
    so_chinh_phuong = []

    for num in tao_danh_sach:
        if math.isqrt(num) ** 2 == num:
            so_chinh_phuong.append(num)

    if so_chinh_phuong:
        return so_chinh_phuong
    else:
        return "Không có số chính phương trong danh sách"
