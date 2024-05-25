def pt_bac_nhat_1_an(a,b):
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        x = -b / a
        return x

import math
def pt_bac_2(a,b,c):
    delta = b**2 - 4*a*c
    if a == 0:
        x = -c / b
        return x
    if a + b + c == 0:
        x1 = 1 ; x2 = c / a
        return f"Phương trình có nghiệm: x1 = {x1}, x2 = {x2}"
    if a - b + c == 0:
        x1 = -1 ; x2 = -c / a
        return f"Phương trình có nghiệm: x1 = {x1}, x2 = {x2}"
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x0 = -b / 2*a
        return f"Phương trình có nghiệm kép: x1 = x2 = {x0}"
    else:
        return "Phương trình vô nghiệm"