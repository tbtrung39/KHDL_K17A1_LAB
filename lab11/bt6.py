bang_so = [
    [4],
    [211, 133, 180, 5],
    [192, 168, 1, 254],
    [11, 1, 11, 233]
]

# Ghi dữ liệu vào tệp bang_so.txt
with open("bang_so.txt", mode = "w") as file:
    for row in bang_so:
        file.write(' '.join(map(str, row)) + '\n')

# Đọc dữ liệu từ tệp bang_so.txt
with open("bang_so.txt", mode = "r") as f:
    lines = f.readlines()
    print("Dong dau tien cua bang so la:")
    print(lines[0])
    print("Dong thu 3 cua bang so la:")
    print(lines[2])

print("Noi dung toan bo file la:")
for row in bang_so:
    print(' '.join(map(str, row)))

# Ghi dữ liệu vào tệp ODD.txt
with open("ODD.txt", mode = "w") as f:
    for row in bang_so:
        so_le = []
        for num in row:
            if num % 2 != 0:
                so_le.append(str(num))
            else:
                so_le.append("0")
        f.write(' '.join(so_le) + '\n')

# Đọc dữ liệu từ tệp ODD.txt
with open("ODD.txt", mode = "r") as f:
    print("Noi dung dong cuoi file ODD.txt la:")
    print(f.readlines()[-1])