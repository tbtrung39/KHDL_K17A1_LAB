def validate_input(input_str):
    if not input_str.isalpha():
        raise ValueError("Lỗi ký tự !!!")

    for i in range(len(input_str) - 1):
        if input_str[i] == input_str[i + 1]:
            raise ValueError("Lỗi nhập liệu !!!")

    for i in range(len(input_str) - 3):
        if input_str[i] == input_str[i + 1] == input_str[i + 2] == input_str[i + 3]:
            raise ValueError("Lỗi nhập lặp lại !!!")

    words = input_str.split()
    for i in range(len(words) - 4):
        if words[i] == words[i + 1] == words[i + 2] == words[i + 3] == words[i + 4]:
            raise ValueError("Lỗi nhập trùng lặp!!!")

while True:
    try:
        user_input = input("Nhập chuỗi ký tự: ")
        validate_input(user_input)
        print(f"Chuỗi hợp lệ: {user_input}")
    except ValueError as ve:
        print(f"{ve}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")