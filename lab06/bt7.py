import random
List_ = [["mon",73],["tue",89],["wed",95],["thu",103],
         ["fri",115],["sat",128],["sun",120]]
print("Danh sách List_: ",List_)
phan_tu = List_[2][1]
print("Phần tử thứ 2, thuộc vị trí thứ 3: ",phan_tu)
List_.append(["rain",random.randint(50,100)])
print("Độ dài List _ ",len(List_))
print("List_ sau khi thêm sublist ngẫu nhiên: ",List_)
a = List_[0][1:3]
b = List_[1][1:3]
c = List_[5][1:3]
d = List_[6][1:3]
sale_value = a + b + c + d
print(f"Tổng sale value của bốn ngày thứ 2,3,7,chủ nhật = {sum(sale_value)}")