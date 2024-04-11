list = []
while True:
    num = int(input("nhập dữ liệu cho đến khi nhập 0 để kết thúc:"))
    if num == 0:
        break
    list.append(num)
chuoi_a = [num for num in list if num >0]
chuoi_b = [num for num in list if num <= 0]
tong = chuoi_a + chuoi_b
m = int(input("nhập số m chèn vào:"))
list.insert(0, m)  
list.insert(4, m)  
print("Danh sách sau khi chuyển các phần tử dương lên đầu:")
print(list)