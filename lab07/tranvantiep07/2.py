number = []
while True : 
    sotn = int(input("Nhap so tu nhien : "))
    if sotn < 0 : 
        print("Nhap lai di !!!")
    else: 
        number.append(sotn)
        break 
A = set(number)
print("Tap A : ", A)
