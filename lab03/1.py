n = int(input("Nhập số n: "))
tong = 1
phan_so = 1
if n > (-3/2):    
    for i in range(0,n+1):
        tu_so = 2*(i+1)
        mau_so = 2*i + 3
        phan_so *= tu_so / mau_so
        tong += phan_so
print("Kết quả =", round(tong,3))