# tìm ước chunh lớn nhất của a và b 
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 36
num2 = 48
gcd = find_gcd(num1, num2)

print("Ước chung lớn nhất của", num1, "và", num2, "là:", gcd)
