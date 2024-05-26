# phuongtrinh.py

import math

def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        x = -b / a
        return x

def giai_phuong_trinh_bac_hai(a, b, c):
    if a == 0:
        return giai_phuong_trinh_bac_nhat(b, c)
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Phương trình vô nghiệm"
        elif delta == 0:
            x = -b / (2*a)
            return x
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return x1, x2
