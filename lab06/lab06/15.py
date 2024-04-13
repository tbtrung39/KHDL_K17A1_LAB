n = int(input("Nhập số lượng tuple: "))
tuples = []
for i in range(n):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    score = float(input("Nhập điểm số: "))
    tuples.append((name, age, score))
tuples.sort(key=lambda x: (x[0], x[1], x[2]))
print("Các tuple sau khi được sắp xếp:")
for tup in tuples:
    print(tup)
