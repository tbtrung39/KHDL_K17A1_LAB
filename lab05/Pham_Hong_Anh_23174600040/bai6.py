chuoi = input("Nhập chuỗi: ")

hex_digits = '0123456789ABCDEF'
hex_values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


chuoi_hex = ''
for char in chuoi:
    if char.upper() in hex_digits:
        chuoi_hex += char


decimal_value = 0
for char in chuoi_hex:
    decimal_value = decimal_value * 16 + hex_values[char.upper()]

print("Giá trị thập phân của chuỗi Hex là:  ", decimal_value)