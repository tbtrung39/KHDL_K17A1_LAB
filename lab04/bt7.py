m = int(input("Nhập giá trị m: "))
n = int(input("Nhập giá trị n: "))
bcnn = m
if m < n:
    temp = m ; m = n ; n = temp 
while True:
    if bcnn % m == 0 and bcnn % n == 0:
        break
    bcnn += 1
print(f"Bội chung nhỏ nhất là ",bcnn)