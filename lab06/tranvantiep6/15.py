# Nhập dữ liệu từ người dùng
num_tuples = int(input("Nhập số lượng tuple: "))
tuples = []
for i in range(num_tuples):
 name = input(f"Nhập tên người thứ {i+1}: ")
 age = int(input(f"Nhập tuổi của {name}: "))
 score = int(input(f"Nhập điểm số của {name}: "))
 tuples.append((name, age, score))

# Sắp xếp tuple theo tên, tuổi, điểm số
tuples.sort(key=lambda x: (x[0], x[1], x[2]))

# In kết quả
print("Danh sách tuple sau khi sắp xếp:")
for t in tuples:
 print(f"Tên: {t[0]}, Tuổi: {t[1]}, Điểm số: {t[2]}")