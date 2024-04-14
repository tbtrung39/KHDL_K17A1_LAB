# Nhập danh sách các số tự nhiên
numbers = []
while True:
    num = int(input("Nhập số tự nhiên (nhập 0 để kết thúc): "))
    if num == 0:
        break
    numbers.append(num)

# Chuyển các phần tử dương lên đầu danh sách
positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num <= 0]
numbers = positive_numbers + negative_numbers

# In danh sách
print("Danh sách sau khi chuyển các phần tử dương lên đầu:", numbers)

# Chèn số m vào đầu, cuối và vị trí thứ 5 của danh sách
m = int(input("Nhập số m: "))
numbers.insert(0, m)
numbers.append(m)
numbers.insert(4, m)

# In danh sách sau khi chèn số m
print("Danh sách sau khi chèn số m:", numbers)