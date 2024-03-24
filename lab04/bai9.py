so = int(input("Nhập một số: "))
tong = 0
while so > 0:
    hang = so % 10  
    tong += hang        
    so //= 10      
print("Tổng các chữ số của số vừa nhập là:", tong)