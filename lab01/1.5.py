a = float(input("Nhập hệ số a của phương trình bậc hai: "))
b = float(input("Nhập hệ số b của phương trình bậc hai: "))
c = float(input("Nhập hệ số c của phương trình bậc hai: "))
x_dinh = -b / (2 * a)
y_dinh = a * x_dinh ** 2 + b * x_dinh + c
x_dinh = round(x_dinh, 2)
y_dinh = round(y_dinh, 2)
dinh = (x_dinh, y_dinh)
print('dinh cua phuong trinh bac 2 la: ', dinh)