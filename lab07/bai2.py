Numbers = {}
while True:
    num_input = input("Nhập số tự nhiên (nhấn Enter để kết thúc): ")
    if num_input == "":
        break
    try:
        num = int(num_input)
        if num < 0:
            print("Vui lòng nhập số tự nhiên dương.")
        else:
            Numbers[num] = None  
    except ValueError:
        print("Vui lòng nhập số tự nhiên hợp lệ.")
print("Danh sách Numbers:", set(Numbers))
