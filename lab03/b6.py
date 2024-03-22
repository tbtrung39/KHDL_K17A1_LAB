n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
        print("Vui lòng nhập số nguyên dương.")
else:
    s=0
    for i in range(0,n+1):
        s+=i**3
    print("tổng bậc 3 của n số nguyên đầu tiên là:",s)