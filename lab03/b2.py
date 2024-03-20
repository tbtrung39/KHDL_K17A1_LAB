n = int(input("nhap vao so nguyen duong: "))
for i in range(n-1,0,-1):
    s=0
    for j in range(1,i):
        if i % j==0:
            s=s+j
        if s == i:
            print(i,"la so hoan hao nho hon n")
            break