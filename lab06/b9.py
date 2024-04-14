danh_sach = []

while True:
    so = input("Nhập một số nguyên (nhấn Enter để kết thúc): ")
    if so == "":
        break
    danh_sach.append(int(so))

for so in danh_sach:
    assert so % 2 == 0, f"Số {so} không phải là số chẵn"
   
print("Tất cả các số trong danh sách là số chẵn")
