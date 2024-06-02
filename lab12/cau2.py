def input_and_check_sequence():
    try:
        input_string = input("Nhập một chuỗi ký tự: ")
        for i in range(len(input_string) - 1):
            if input_string[i] == input_string[i + 1]:
                raise Exception("Lỗi nhập lặp lại!!!")
        for i in range(len(input_string) - 4):
            if len(set(input_string[i:i+5])) == 1:
                raise Exception("Lỗi nhập lặp lại!!!")
    except Exception as e:
        print(e)
    else:
        print("Chuỗi nhập hợp lệ.")
    finally:
        print("Kết thúc kiểm tra.")

# Gọi hàm kiểm tra
input_and_check_sequence()