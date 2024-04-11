# Nhập danh sách các tuple (name, age, score) từ người dùng
danh_sach = []
n = int(input("Nhập số lượng tuple: "))
for _ in range(n):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    score = float(input("Nhập điểm: "))
    danh_sach.append((name, age, score))

# Sắp xếp danh sách theo name, age, score
sap_xep = sorted(danh_sach, key=lambda x: (x[0], x[1], x[2]))

# In ra danh sách đã sắp xếp
print("Danh sách đã sắp xếp:")
for i in sap_xep:
    print(i)
