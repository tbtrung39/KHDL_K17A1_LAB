import math

def giai_pt_bac_nhat(a, b):
    """Giải phương trình bậc nhất ax + b = 0."""
    if a == 0:
        if b == 0:
            return "Phương trình bậc nhất có vô số nghiệm"
        else:
            return "Phương trình bậc nhất vô nghiệm"
    else:
        x = -b / a
        return f"Nghiệm của phương trình bậc nhất là là: x = {x}"

def giai_pt_bac_hai(a, b, c):
    """Giải phương trình bậc hai ax^2 + bx + c = 0."""
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình bậc hai vô nghiệm"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"