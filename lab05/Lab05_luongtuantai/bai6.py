str=input("Nhập chuỗi ký tự hệ hex: ")
la_hex = True
for char in str:
    if not (('0' <= char <= '9') or ('A' <= char <= 'F')):
        la_hex = False
        break
if la_hex:
    print("Đây là một chuỗi hex hợp lệ.")
else:
    print("Đây không phải là một chuỗi hex hợp lệ.")

gia_tri_he_10=0
for digit in str:
    if '0' <= digit <= '9':
        gia_tri_he_10 = gia_tri_he_10 * 16 + int(digit)
    elif 'A' <= digit <= 'F':
        gia_tri_he_10 = gia_tri_he_10 * 16 + ord(digit) - ord('A') + 10
print("Giá trị thập phân của số hex là:", gia_tri_he_10)