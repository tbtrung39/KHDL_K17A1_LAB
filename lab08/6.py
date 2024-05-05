import math
def boi_chung_nho_nhat(a,b):
    return (a*b)/math.gcd(a,b)
so_a= int(input("nhập giá trị của a:"))
so_b = int(input("nhập giá trị của b:"))
bcnn  = boi_chung_nho_nhat(so_a,so_b)
print("bội chung nhỏ nhất của 2 số là:",bcnn) # gcd trả về ước chung lớn nhất của 1 hoặc nhiều số nguyên 
