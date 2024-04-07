n = input("Nhập chuỗi:")
loi = 0
for char in n:
    if char.isalpha():
        n += 1
print("Số các chữ cái TA là:",n)