danh_sach = input("Nhập các số, cách nhau bằng dấu phẩy: ").split(',')
danh_sach = [int(x.strip()) for x in danh_sach]
for i in danh_sach:
    assert i % 2 == 0, f"{i} không phải là số chẵn"
print("Các số là số chẵn")