numbers = []
while True:
        num = int(input("Nhập một số tự nhiên (nhập 0 để dừng): "))
        if num == 0:
            break
        numbers.append(num)
set_A = set(numbers)
print("Tập hợp A được tạo từ danh sách số nhập từ bàn phím là:", set_A)
