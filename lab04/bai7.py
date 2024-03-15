m = int(input("nhập m: "))
n = int(input("Nhập n: "))
if m < n:
    temp = m ; m = n ; n = temp
while(m!=n):
    p = m -n
    if p > n:m=p
    else:
        m=n
        n=p
        
bcnn = (m*n) / m
print("bội chung nhỏ nhất là: ", bcnn)