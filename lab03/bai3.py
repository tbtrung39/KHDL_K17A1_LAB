n = int(input("Nhap vao mot so nguyen duong n:"))
for i in range(n,1,-1):
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        print("cac so nguyen to nho hon hoac bang n la:",i)