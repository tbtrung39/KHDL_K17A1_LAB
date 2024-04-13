tuple = []
n = int(input("Nhập số lượng tuple bạn muốn nhập: "))
for i in range(n):
    name = str(input("Nhập tên người dùng: "))
    age = int(input("Nhập tuổi của người dùng: "))
    score = float(input("Nhập điểm của người dùng: "))
    tuple.append((name, age, score))
sorted_data = sorted(tuple, key=lambda x: (x[0], x[1], x[2]))
print("Danh sách các tuple sau khi được sắp xếp:")
for item in sorted_data:
    print(item)