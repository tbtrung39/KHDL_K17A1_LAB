#2
numbers = []
while True:
    so = input("Nhập số tự nhiên (Nhập 'xong' để kết thúc): ")
    if so == 'xong':
        break
    if so.isdigit(): 
        numbers.append(int(so))
    else:
        print("Vui lòng nhập số tự nhiên.")
A = set(numbers)
print("Danh sách Numbers:", numbers)
print("Tập hợp A:", A)
