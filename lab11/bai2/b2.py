import csv
with open(file = r"lab11\bai2\Inp.txt",mode = "r") as file:
    line = file.read().strip()

    line = line.replace(" ", ",")

# Sử dụng csv.reader để đọc dữ liệu đã thay đổi
list_read = list(csv.reader([line]))

# Chuyển đổi chuỗi các số thành danh sách các số nguyên
numbers = [int(num) for num in list_read[0]]

# Sắp xếp danh sách các số theo thứ tự tăng dần
numbers.sort()

# Ghi danh sách đã sắp xếp vào tệp tin out.dat
with open(r"lab11\bai2\out.dat", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(numbers)