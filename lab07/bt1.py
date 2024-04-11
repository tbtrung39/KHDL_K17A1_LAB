# Khởi tạo một set rỗng
char_set = set()

# Nhập dữ liệu từ bàn phím
while True:
    char = input("Nhập ký tự (Nhấn ESC để kết thúc): ")
    
    # Kiểm tra nếu ký tự là ESC thì dừng vòng lặp
    if char == chr(27):
        break
    
    # Thêm ký tự vào set
    char_set.add(char)

# Xóa các ký tự số khỏi set
char_set = {char for char in char_set if not char.isdigit()}

# In ra set sau khi loại bỏ các ký tự số
print("Set sau khi loại bỏ các ký tự số:", char_set)