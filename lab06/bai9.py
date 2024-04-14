
danh_sach = [int(x) for x in input("Nhập các số nguyên cách nhau bằng dấu cách: ").split()]
for num in danh_sach:
    assert num % 2 == 0, f"{num} không phải là số chẵn."

print("Tất cả các số trong danh sách là số chẵn.")
