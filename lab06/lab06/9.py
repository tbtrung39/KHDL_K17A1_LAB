danh_sach = input("Nhập các số chẵn cách nhau bằng dấu phẩy: ").split(',')
danh_sach = [int(x.strip()) for x in danh_sach]
for so in danh_sach:
    assert so % 2 == 0, f"Số {so} không phải là số chẵn."
print("Tất cả các số trong danh sách là số chẵn.")
