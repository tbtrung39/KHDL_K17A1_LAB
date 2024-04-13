import random

# Danh sách ban đầu
List = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

# In các phần tử của List ra màn hình
print("Danh sách List_:")
for item in List:
    print(item)

# Phần tử thứ hai của sublist
sublist = List[1][1]
print("Phần tử thứ hai của sublist:", sublist)

# Thêm một sublist ngẫu nhiên
ran_sublist = ["random", random.randint(50, 150)]
List.append(ran_sublist)
print("List_ sau khi thêm một sublist ngẫu nhiên:", List)

# Tính tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật
tong = sum(item[1] for item in List[1::2])
print("Tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật:", tong)