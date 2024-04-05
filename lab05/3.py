n = int(input("Nhap so tu nhien: "))
nhi_phan = ""
while n < 0:
    n = int(input("Nhap lai n: "))
while n > 0:
    a = n%2
    nhi_phan =  str(a) + nhi_phan
    n//=2
print("Chuoi nhi phan: ", nhi_phan)