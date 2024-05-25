import math
def pt_bac_nhat(m, n):
    if  m == 0:
        print("Day khong phai la phuong trinh bac nhat")
    else:
        print(f"Phuong trinh co nghiem duy nhat: x = {(-n) / (m)}")

def pt_bac_hai(a, b, c):
    delta = b * b - 4 * a * c
    if delta == 0:
        x = -b / (2 * a)
        print(f"Phuong trinh co nghiem kep x1 = x2 = {x}")
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phuong trinh co hai nghiem phan biet la x1 = {x1} va x2 = {x2}")
    else:
        print("phuong trinh vo nghiem")
        