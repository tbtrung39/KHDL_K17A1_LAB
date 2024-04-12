list_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print(f"Danh sach {list_}")
print(f"Phan tu thu 2 thuoc vi tri thu 3 la {list_[3][1:3]}")
print(f"Do dai cua list_ = {len(list_)}")
m = ["mer", 1904]
list_.append(m)
print(f"Sau khi them mot sublist ngau nhien {list_}")
a = list_[0][1:3]
b = list_[1][1:3]
c = list_[5][1:3]
d = list_[6][1:3]
sale_value = a + b + c + d
print(f"Tong sale value cua bon ngay thu 2,3,7,chu nhat = {sum(sale_value)}")
