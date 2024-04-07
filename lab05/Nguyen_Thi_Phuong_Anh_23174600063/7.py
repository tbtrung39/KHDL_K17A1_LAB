str = input("Nhập đoạn văn bản hoàn chỉnh: ")
tu_khoa = str.split()
dem = 0
for tu in tu_khoa:
    if len(tu.split()) == 1:
        dem += 1
print("Số lần xuất hiện của các từ đơn trong đoạn văn bản là:", dem)