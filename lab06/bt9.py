lst = input("Nhập danh sách các số (cách nhau bằng dấu phẩy): ").split(',')
lst = [int(num) for num in lst]

# Xác minh rằng tất cả các số trong danh sách là chẵn
for num in lst:
    assert num % 2 == 0, f"Số {num} không phải là số chẵn"

print("Tất cả các số trong danh sách đều là số chẵn.")
