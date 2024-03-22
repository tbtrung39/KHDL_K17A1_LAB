#câu 9 tính tổng dãy số
tong = 0
n = int(input("nhập số n:"))
if n >0:
    for i in range (1,n+1):
        tong += i**2
    print(tong)  
else:
    print("nhập lại để n > 0")
#b)
tong = 0
n = int(input("nhập số n:"))
if n >0:
    for i in range (1,n,2):
        tong += i**3 + (2*n+1)**3
    print(tong)
else:
    print("nhập lại để n > 0")
#c)
tong = 0
n = int(input("nhập số n:"))
if n >0:
    for i in range (2,n,2):
        tong += i**4 + (2*n)**4
    print(tong)
else:
    print("nhập lại để n > 0")
