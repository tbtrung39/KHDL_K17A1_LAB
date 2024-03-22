#câu 8 tính tổng dãy số
#a)
tong = 0
n = int(input("nhập số n:"))
if n >0:
    for i in range (1,n+1):
        tong += i
    print(tong)  
else:
    print("nhập lại để n > 0")
#b)
tong = 0
n = int(input("nhập số n:"))
if n >0:
    for i in range (1,n,2):
        tong += i + (2*n+1)
    print(tong)
else:
    print("nhập lại để n > 0")
#c)
tong = 0
n = int(input("nhập số n:"))
if n >0:
    for i in range (2,n,2):
        tong += i + (2*n)
    print(tong)
else:
    print("nhập lại để n > 0")
