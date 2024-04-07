
text = input("Nhập đoạn văn bản: ")
tu = input("Nhập từ đơn cần tìm: ")
tu_trong_van_ban = text.split()
so_lan_xuat_hien = sum(1 for word in tu_trong_van_ban if word.lower() == tu.lower())
print("Số lần xuất hiện của từ đơn trong chuỗi:", so_lan_xuat_hien)