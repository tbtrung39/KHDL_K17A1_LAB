import math

def giai_pt_bac_hai(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x,
    else:
        return "Phương trình vô nghiệm"

# Nhập các hệ số từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Gọi hàm giải phương trình bậc hai và in ra kết quả
nghiem = giai_pt_bac_hai(a, b, c)
print("Nghiệm của phương trình là:")
for i, sol in enumerate(nghiem):
    print(f"Nghiệm {i+1}: {sol}")