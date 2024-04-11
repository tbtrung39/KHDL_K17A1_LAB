Numbers = []
while True:
    num_str = input("Nhập số tự nhiên (Nhấn Enter để dừng): ")
    if num_str == "":
        break
    Numbers.append(int(num_str))

# Tạo tập hợp A từ danh sách Numbers bằng cách sử dụng set
A = set(Numbers)

# In ra tập hợp A
print("Tập hợp A:", A)
