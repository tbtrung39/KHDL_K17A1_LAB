a = int(input("Giá trị a của phương trình bậc 2:"))
b = int(input('Giá trị b của phương trình bậc 2:'))
c = int(input("Giá trị c của phương trình bậc 2:"))
x_dinh = -b/2*a
y_dinh = a*(x_dinh)**2+b*x_dinh+c
print("Đỉnh của phương trình bậc 2 là:","(",x_dinh,y_dinh,")")