import random

size = int(input("Nhập kích thước của tập hợp A: "))

A = set()
for _ in range(size):
    choice = random.choice(["integer", "float", "string"])
    if choice == "integer":
        A.add(random.randint(-100, 100))
    elif choice == "float":
        A.add(round(random.uniform(-100, 100), 2))  
    else:
        length = random.randint(1, 10)  
        string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))  
        A.add(string)

# Đếm số nguyên, số thực và chuỗi ký tự
integer_count = 0
float_count = 0
string_count = 0

for element in A:
    if isinstance(element, int):
        integer_count += 1
    elif isinstance(element, float):
        float_count += 1
    elif isinstance(element, str):
        string_count += 1

# In kết quả
print("Tập hợp A bao gồm:")
for element in A:
    print(element)

print("\nSố lượng số nguyên trong tập hợp A:", integer_count)
print("Số lượng số thực trong tập hợp A:", float_count)
print("Số lượng chuỗi ký tự trong tập hợp A:", string_count)


