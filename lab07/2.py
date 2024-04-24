number_list = []
while True:
    number = input("Nhập số tự nhiên (nhấn Enter để kết thúc): ")
    if number == '':
        break
    try:
        number_list.append(int(number))
    except ValueError:
        print("Vui lòng chỉ nhập số tự nhiên.")

# Sinh ra tập hợp a với các thuộc tính của danh sách number_list
a = set(number_list)

print("Danh sách số tự nhiên:", number_list)
print("Tập hợp a:", a)