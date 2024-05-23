import math

def giai_pt_bac2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phuong trinh vo so nghiem"
            else:
                return "Phuong trinh vo nghiem"
        else:
            x = -c / b
            return f"Nghiem cua phuong trinh la: {x}"
    else:
        delta = b**2 - 4 * a * c
        if delta < 0:
            return "Phuong trinh vo nghiem"
        elif delta == 0:
            x = -b / (2 * a)
            return f"Phuong trinh co nghiem kep: {x}"
        else:
            sqrt_delta = math.sqrt(delta)
            x1 = (-b + sqrt_delta) / (2 * a)
            x2 = (-b - sqrt_delta) / (2 * a)
            return f"Phuong trinh co hai nghiem phan biet: {x1} va {x2}"


