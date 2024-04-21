char_set = set()
while True:
    char = input("Nhập ký tự (Nhấn ESC để kết thúc): ")

    if char == chr(27):
        break
    char_set.add(char)
char_set = {char for char in char_set if not char.isdigit()}
print("Set sau khi loại bỏ các ký tự số:",char_set)