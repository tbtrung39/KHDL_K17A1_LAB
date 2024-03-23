tong = 1 
n = int(input("Nhap n: "))
for i in  range(n+1):
    tich = 1
    for j in range(i+1):
        tich*=2*(j+1)/(2*j+3)
        tong += tich
print(f"ket qua la: {tong:.3f}")