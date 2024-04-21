Numbers = []
while True:
    num_str = input("Nhập số tự nhiên (Nhấn Enter để dừng): ")
    if num_str == "":
        break
    Numbers.append(int(num_str))
A = set(Numbers)
print("Tập hợp A:",  A)