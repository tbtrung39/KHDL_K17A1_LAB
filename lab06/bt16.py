x = int(input("Nhập giá trị x: "))
y = int(input("Nhập giá trị y: "))
list_cha = [[i*j for j in range(0,y)] for i in range(0,x)]
print(list_cha)