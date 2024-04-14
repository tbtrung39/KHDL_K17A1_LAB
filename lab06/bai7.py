List = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

print("Danh sách ban đầu:")
for item in List:
    print(item)

if len(List) >= 3 and len(List[2]) >= 2:
    phan_tu_sublist = List[2][1]
    print("\nPhần tử thứ hai của sublist thứ 3:", phan_tu_sublist)
else:
    print("\nKhông có phần tử thứ hai của sublist thứ 3.")

import random
sublist_moi = ["new", random.randint(50, 150)]
List.append(sublist_moi)

cac_ngay_can_tinh_toan = ["tue", "wed", "sat", "sun"]
tong_sale_value = 0
for ngay in cac_ngay_can_tinh_toan:
    for item in List:
        if item[0] == ngay:
            tong_sale_value += item[1]

print("\nTổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật là:", tong_sale_value)
