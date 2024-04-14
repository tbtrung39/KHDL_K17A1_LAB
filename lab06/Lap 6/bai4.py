my_list = []
while True:
    num = int(input("Nhập số tự nhiên (nhập 0 để dừng): "))
    if num == 0:
        break
    my_list.append(num)

# Chèn danh sách [1, 2, 3] vào vị trí đầu, cuối và thứ 5
my_list = [1, 2, 3] + my_list
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.insert(4, 1)
my_list.insert(5, 2)
my_list.insert(6, 3)

print("Danh sách sau khi chèn:", my_list)

# Xóa phần tử thứ k
k = int(input("Nhập vị trí phần tử cần xóa: "))
del my_list[k-1]
print("Danh sách sau khi xóa phần tử thứ", k, ":", my_list)

# Sắp xếp danh sách tăng dần và giảm dần
my_list.sort()
print("Danh sách sắp xếp tăng dần:", my_list)

my_list.sort(reverse=True)
print("Danh sách sắp xếp giảm dần:", my_list)