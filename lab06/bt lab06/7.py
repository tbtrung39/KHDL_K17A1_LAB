import random

List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Danh sách List_:", List_)
phần_tử_thứ_hai = List_[1][1]
print("Phần tử thứ hai:", phần_tử_thứ_hai)
độ_dài = len(List_)
sublist_ngẫu_nhiên = ["random", random.randint(50, 150)]
List_.append(sublist_ngẫu_nhiên)
print("List_ sau khi thêm một sublist ngẫu nhiên:", List_)
tổng_sale_value = 0
for sublist in List_:
    if sublist[0] in ["tue", "wed", "sat", "sun"]:
        tổng_sale_value += sublist[1]

print("Tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật:", tổng_sale_value)
