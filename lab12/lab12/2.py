try:
    user_input = input("Nhập chuỗi ký tự: ")
    
    # Check if the input is a number
    if user_input.isdigit():
        raise ValueError("Lỗi ký tự: Chuỗi không được là số!!!")
    
    # Check for any four consecutive identical characters
    for i in range(len(user_input)):
        if i < len(user_input) - 4:
            if user_input[i] * 4 == user_input[i:i + 4]:
                raise ValueError("Lỗi nhập liệu: Có 4 ký tự liên tiếp giống nhau!!!")
    
    # Check for any three consecutive identical characters
    for i in range(len(user_input)):
        if i < len(user_input) - 3:
            if user_input[i] * 3 == user_input[i:i + 3]:
                raise ValueError("Lỗi nhập liệu: Có 3 ký tự liên tiếp giống nhau!!!")
    
    # Check for any two consecutive identical characters
    for i in range(len(user_input)):
        if i < len(user_input) - 2:
            if user_input[i] * 2 == user_input[i:i + 2]:
                raise ValueError("Lỗi nhập liệu: Có 2 ký tự liên tiếp giống nhau!!!")

except ValueError as er:
    print("Lỗi:", er)
finally:
    print("Chương trình tiếp tục hoạt động")
