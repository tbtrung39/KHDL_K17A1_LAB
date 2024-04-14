# Nhập danh sách các tuple từ người dùng
danh_sach = []
while True:
    nhap = input("Nhập (name, age, score) hoặc nhấn Enter để kết thúc: ")
    if nhap == "":
        break
    name, age, score = nhap.split(", ")
    danh_sach.append((name, int(age), float(score)))

# Sắp xếp danh sách theo tiêu chí: name -> age -> score
danh_sach_sap_xep = sorted(danh_sach, key=lambda x: (x[0], x[1], x[2]))

# In danh sách đã sắp xếp
print("Danh sách sau khi sắp xếp:")
for item in danh_sach_sap_xep:
    print(item)
