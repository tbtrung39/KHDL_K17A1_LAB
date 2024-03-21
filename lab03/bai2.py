n = int(input("Nhap vao mot so n:"))
for i in range(n,1,-1):
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        print("so nguyen to gan nhat la:",i)
        break