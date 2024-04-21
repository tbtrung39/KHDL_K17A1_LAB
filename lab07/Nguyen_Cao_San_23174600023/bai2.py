# Khởi tạo danh sách numbers
numbers = []

print("Nhập các số tự nhiên, ấn Enter để nhập số mới và ấn Enter khi hoàn thành:")

while True:
    num = input("Nhập số tự nhiên (ấn Enter để kết thúc): ")
    if num == "":
        break 
    
   
    if num.isdigit():
        numbers.append(int(num))
    else:
        print("Vui lòng nhập một số tự nhiên.")

a = set(numbers)

print("Danh sách các số tự nhiên:", numbers)
print("Tập hợp a:", a)
