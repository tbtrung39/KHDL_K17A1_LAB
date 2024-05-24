def giaiPTBacNhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        return "Nghiệm của phương trình là: x = " + str(-b/a)

def giaiPTBacHai(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2*a)
        return "Phương trình có nghiệm kép: x1 = x2 = " + str(x)
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return "Phương trình có hai nghiệm phân biệt: x1 = " + str(x1) + ", x2 = " + str(x2)