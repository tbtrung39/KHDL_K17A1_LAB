#câu 1
#a)
n = int(input("nhập số nguyên dương n:"))
tong = 0
while True:
    if n <= 0 :
        print("vui lòng nhập lại n")
    else:
        for i in range (1, n+1):
            tong += i**2 
            print(f"tổng các số là {tong}")
    break
print(f"tổng của tất cả các phần tử < n là {tong}")
#b)
n = int(input("nhập số nguyên dương n:"))
tong = 0
while True:
    if n <= 0 :
        print("vui lòng nhập lại n")
        break
    else:
        for i in range (1, n,2):
            tong += i**3 + (2*n + 1)**3
            print(f"tổng các số là {tong}")
        break
print(f"tổng của tất cả các phần tử < n là {tong}")
#c)
n = int(input("nhập số nguyên dương n:"))
tong = 0
while True:
    if n <= 0 :
        print("vui lòng nhập lại n")
        break
    else:
        for i in range (2, n ,2):
            tong += i**4 + (2*n)**4
            print(f"tổng các số là {tong}")
        break
print(f"tổng của tất cả các phần tử < n là {tong}")
