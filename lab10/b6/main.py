from pk6 import convert_binary_to_decimal,convert_hexadecimal_to_decimal,convert_octal_to_decimal,determine_base,remove_invalid_characters
input_string=int(input("nhập vào 1 chuỗi số:"))
print(convert_binary_to_decimal(input_string))
print(convert_hexadecimal_to_decimal(input_string))
print(convert_octal_to_decimal(input_string))
print(determine_base(input_string))
print(remove_invalid_characters(input_string))