x = int(input("Nhap vao gia tri x: "))
y = int(input("Nhap vao gia tri y: "))
list_cha = [[i*j] for j in range(0, y) for i in range(0, x)]
print(list_cha)