def check_binary_numbers(input_string):
    binaries = input_string.split(',')
    result = [b for b in binaries if int(b, 2) % 5 == 0]
    return ','.join(result)

input_string = input("Nhập chuỗi các số nhị phân, phân tách bởi dấu phẩy: ")
result = check_binary_numbers(input_string)
print(result)