m = int(input("Nhập giá trị m: "))
n = int(input("Nhập giá trị n: "))
if m < n:
    p = m;m = n;n = p
while m != n:
    q = m - n
    if q > n: m = q
    else:
        m = n
        n = q
ucln = m
bcnn = (m*n) // ucln
print(f"Bội chung nhỏ nhất là ",bcnn)