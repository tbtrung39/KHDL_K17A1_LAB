x = int(input("nhập giá trị x: "))
y = int(input("Nhập giá trị y: "))
list = []
for i in range(0, x):
    new_list = []
    for j in range(0,y):
        kq = i * j
        new_list.append(kq)
    list.append(new_list)
print(list)