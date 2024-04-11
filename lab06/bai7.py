List_ = [["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
print(f"danh sách {List_}")
print(f"phần tử thứ 2 thuộc vị trí thứ 3 là {List_[3][1:3]}")
print(f"độ dài của List_ = {len(List_)}")
m = ["mer",1904]
List_.append(m)
print(f"sau khi thêm một sublist ngẫu nhiên {List_}")
a = List_[0][1:3]
b = List_[1][1:3]
c = List_[5][1:3]
d = List_[6][1:3]
sale_value = a + b + c + d
print(f"tổng sale value của bốn ngày thứ 2,3,7,chủ nhật = {sum(sale_value)}")