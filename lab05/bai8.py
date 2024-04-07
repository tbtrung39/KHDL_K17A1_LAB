Str = input("Nhập đoạn văn bản hoàn chỉnh: ")
vanban = Str.split()
tong = 0

for tu in vanban:
    if len(tu) == 1:
        tong += 1
print("Số lượng từ đơn trong đoạn văn bản là:", tong)
