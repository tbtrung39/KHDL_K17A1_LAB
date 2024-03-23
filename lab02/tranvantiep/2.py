a = float(input("Nhap a : "))
b = float(input("Nhap b : "))
c = float(input("NHap c : "))
delta = b**2 - 4 * a * c 
if delta == 0 : 
    print("phuong trinh co nghiem kep  : ", -b / (2 * a))
elif delta > 0 : 
    print("phuong trinh có hai nghiem : ", (-b + delta**0.5)/(2 * a), (-b - delta**0.5)/(2 * a))
else: 
    print("phuong trinh vo nghiem")