import random
import math

def sinh_day_so():
    x=int(input("nhap so phan su cua day: "))
    day_so = [random.randint(1, 100) for i in range(x)]
    return day_so

def hien_thi_day_so(day_so):
    print("day so ngau nhien:", day_so)

def kiem_tra_so_nguyen_to(so):
    if so < 2:
        return False
    for i in range(2, int(math.sqrt(so)) + 1):
        if so % i == 0:
            return False
    return True

def liet_ke_so_nguyen_to_chia_het_cho_7(day_so):
    print("cac so nguyen to chia het cho 7 la:")
    for so in day_so:
        if so % 7 == 0 and kiem_tra_so_nguyen_to(so):
            print(so)

def tinh_tong_so_le(day_so):
    tong = sum(so for so in day_so if so % 2 != 0)
    print("Tong cac so le la:", tong)

def kiem_tra_so_chinh_phuong(so):
    return math.isqrt(so) ** 2 == so

def hien_thi_so_chinh_phuong(day_so):
    chinh_phuong = [so for so in day_so if kiem_tra_so_chinh_phuong(so)]
    if chinh_phuong:
        print("cac so chinh phuong la:", chinh_phuong)
    else:
        print("day so khong co so chinh phuong")