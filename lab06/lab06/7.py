import random
Danh_sách = [["thứ hai", 73], ["thứ ba", 89], ["thứ tư", 95], ["thứ năm", 103], ["thứ sáu", 115], ["thứ bảy", 128], ["chủ nhật", 120]]
print("Các phần tử của Danh_sách_:")
for sublist in Danh_sách:
    print(sublist)
phần_tử_thứ_hai = Danh_sách[2][1]
print("Phần tử thứ hai thuộc vị trí thứ 3 của sublist:", phần_tử_thứ_hai)
sublist_ngẫu_nhiên = ["ngày_mới", random.randint(50, 150)]
Danh_sách.append(sublist_ngẫu_nhiên)
print("Danh_sách_ sau khi thêm một sublist ngẫu nhiên:", Danh_sách)
tổng_sale_value = 0
for sublist in Danh_sách:
    if sublist[0] in ["thứ hai", "thứ ba", "thứ bảy", "chủ nhật"]:
        tổng_sale_value += sublist[1]
print("Tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật là:", tổng_sale_value)
