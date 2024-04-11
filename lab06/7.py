list_ = [["mon", 73], ["tue", 89], ["web", 95], ["web", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách list_ ban đầu:")
for item in list_:
    print(item)
a = list_[2][1]
print("\nPhần tử thứ 2 thuộc vị trí thứ 3 của sublist:", a)
b = ["random", 95]  
list_.append(b)
print("\nDanh sách list_ sau khi thêm một sublist ngẫu nhiên:")
for item in list_:
    print(item)
sum = 0
for item in list_:
    if item[0] in ["mon", "tue", "sat", "sun"]:
       sum += item[1]
print("\nTổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật là:", sum)
