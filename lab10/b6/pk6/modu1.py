def remove_invalid_characters(input_string):
    valid_characters = {'0', '1', '2', '9', 'A', 'B', 'C', 'D', 'E', 'F'}
    filtered_string = ''.join(char for char in input_string if char in valid_characters)
    print("Chuỗi sau khi loại bỏ ký tự không hợp lệ:", filtered_string)

def determine_base(input_string):
    if set(input_string).issubset({'0', '1'}):
        print("Chuỗi số nhập vào được hiểu là cơ số 2.")
    elif set(input_string).issubset({'0', '1', '2', '3', '4', '5', '6', '7'}):
        print("Chuỗi số nhập vào được hiểu là cơ số 8.")
    elif set(input_string).issubset({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'}):
        print("Chuỗi số nhập vào được hiểu là cơ số 16.")
    else:
        print("Không xác định được cơ số của chuỗi số.")

def convert_binary_to_decimal(input_string):
    decimal_value = int(input_string, 2)
    print("Giá trị của chuỗi số {} ở cơ số 10 là: {}".format(input_string, decimal_value))

def convert_octal_to_decimal(input_string):
    decimal_value = int(input_string, 8)
    print("Giá trị của chuỗi số {} ở cơ số 10 là: {}".format(input_string, decimal_value))

def convert_hexadecimal_to_decimal(input_string):
    decimal_value = int(input_string, 16)
    print("Giá trị của chuỗi số {} ở cơ số 10 là: {}".format(input_string, decimal_value))

