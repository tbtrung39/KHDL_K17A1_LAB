def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    return (a * b) // gcd

# Sử dụng hàm find_lcm để tìm BCNN của hai số
num1 = 12
num2 = 18
lcm = find_lcm(num1, num2)

print("Bội chung nhỏ nhất của", num1, "và", num2, "là:", lcm)
