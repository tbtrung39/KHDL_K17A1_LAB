import random
def sinh_day_so():
    a = [random.randint(1, 100) for _ in range(100)]
    print("Dãy số ngẫu nhiên là:", a)
    return a

def liet_ke(danh_sach):
    a = [x for x in danh_sach if x % 7 == 0 and snt(x)]
    print(f"Các số nguyên tố chia hết cho 7 trong dãy là: {a}")

def tinh_tong_so_le(danh_sach):
    tong_so_le = sum([a for a in danh_sach if a % 2 != 0])
    print("Tổng các số lẻ trong dãy là:", tong_so_le)

def kiem_tra_so_chinh_phuong(danh_sach):
    so_chinh_phuong = [a for a in danh_sach if is_perfect_square(a)]
    if so_chinh_phuong:
        print("Các số chính phương trong dãy là:", so_chinh_phuong)
    else:
        print("Không có số chính phương trong dãy.")

def snt(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

