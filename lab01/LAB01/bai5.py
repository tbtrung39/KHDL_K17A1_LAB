#Viết chương trình nhập vào giá trị a, b, c của một phương trình bậc 2.
# Tìm đỉnh của phương trình bậc 2 đó (Làm tròn đến số thập phân thứ hai).   
#bài 5
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
#tọa độ đỉnh x
x = -b / (2 * a)
#tọa độ y tương ứng với x của đỉnh
y = a * x ** 2 + b * x + c
#làm tròn
x=round(x,2)
y=round(y,2)
print("đỉnh của phương trình bậc 2 là:",x,y)
