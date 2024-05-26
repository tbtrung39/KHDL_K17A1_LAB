import math

def giai_phuong_trinh_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Nghiệm của phương trình: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2*a)
        return f"Nghiệm kép của phương trình: x1 = x2 = {x}"
    else:
        return "Phương trình vô nghiệm"
