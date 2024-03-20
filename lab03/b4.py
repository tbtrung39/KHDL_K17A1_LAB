n = int(input("nhap vao so nguyen duong: "))
for i in range(n-1,0,-1):
    for j in range(0,i):
        if j == 0 or j ==1:
            continue
        if  i% j==0:
            break
    else:
        print(f"{i} la so nguyen to be hon hoac bang n")