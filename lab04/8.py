while True:
    char = input("Nhập một ký tự (hoặc nhấn 'q' để thoát): ")
    if char == 'q':
        print("Thoát chương trình.")
        break
    ascii_value = ord(char)
    print(f"Mã ASCII của ký tự '{char}' là: {ascii_value}")
