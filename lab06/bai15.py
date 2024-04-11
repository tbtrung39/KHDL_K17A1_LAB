danh_sach = []
n = int(input("Nhập số lượng tuple: "))
for _ in range(n):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    score = float(input("Nhập điểm: "))
    danh_sach.append((name, age, score))
sap_xep = sorted(danh_sach, key=lambda x: (x[0], x[1], x[2]))
print("Danh sách đã sắp xếp:")
for i in sap_xep:
    print(i)