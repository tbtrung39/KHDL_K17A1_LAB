'''
Giả sử có một danh sách như sau:
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128],["sun", 120]]
Yêu cầu:
- Tạo danh sách List_ và in các phần tử của List_ ra màn hình.
- Chọn ra phần từ thứ hai, thuộc vị trí thứ 3 của sublist.
- Kiểm tra độ dài của list test và thêm một sublist ngẫu nhiên.
- Thực hiện tính toán tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật.
'''
import random
#Tạo danh sách List_ và in các phần tử của List_ ra màn hình
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128],["sun", 120]]
print("Danh sách List_:", List_)

#Chọn ra phần từ thứ hai, thuộc vị trí thứ 3 của sublist
print("Phần tử thứ hai thuộc vị trí thứ ba là:", List_[3][1])

#Kiểm tra độ dài của list test và thêm một sublist ngẫu nhiên
random_sublist = [random.choice(["A", "B", "C"]), random.randint(50, 150)]
List_.append(random_sublist)
print("List_ sau khi thêm một sublist ngẫu nhiên:", List_)

#Tính toán tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật
sum_sales = List_[1][1] + List_[2][1] + List_[5][1] + List_[6][1]
print("Tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật:", sum_sales)


