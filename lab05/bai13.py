# Nhập hai chuỗi ký tự A và B từ người dùng
A = input("Nhập chuỗi ký tự A: ")
B = input("Nhập chuỗi ký tự B: ")

# Tạo tất cả các cặp kết hợp có thể của A và B
combinations = [(A[:i], A[i:], B[:j], B[j:]) for i in range(1, len(A)) for j in range(1, len(B))]

# Kiểm tra từng cặp kết hợp để tìm ra đúng thức toán
found = False
for combo in combinations:
    C, D, E, F = combo
    try:
        if int(C) + int(D) == int(E) + int(F):
            print(f"{C} + {D} = {E} + {F}")
            found = True
            break
    except ValueError:
        pass

# Nếu không tìm thấy cách đặt dấu '+', thông báo không tồn tại cách đặt
if not found:
    print("Không tồn tại cách đặt!")
