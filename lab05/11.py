str = input("Nhap chuoi ky tu nhi phan: ")
binary = True
for char in str:
    if char != '0' and char != '1':
        binary = False
        break
if binary:
    decimal = 0
    for i in range(len(str)):
        decimal += int(str[i])*(2**(len(str)-i-1))
    print("So thap phan tuong ung la:", decimal)
else:
    print("chuoi ky tu ban nhap vao khong phai la chuoi nhi phan")