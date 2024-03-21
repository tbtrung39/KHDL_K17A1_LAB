n = int(input("Nhap vao mot so n:"))
tong = 0
for i in range(1,n):
    if n % i ==0:
        tong +=i
        if tong == n:
            print("end!")
        elif tong < n:
            print("cac so hoan hao nho hon",n,"la",tong)