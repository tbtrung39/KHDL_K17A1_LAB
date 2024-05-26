from pk_11 import (
    doi_sang_nhi_phan, 
    doi_sang_bat_phan, 
    doi_sang_thap_luc_phan,
    remove_invalid_chars,
    get_base,
    convert_to_base10
)

def nhap_so():
    n = int(input("Nhập vào một số nguyên: "))
    return n

# Nhập số từ người dùng
num = nhap_so()

# Sử dụng các hàm từ package pk_11 để chuyển đổi số
binary = doi_sang_nhi_phan(num)
octal = doi_sang_bat_phan(num)
hexadecimal = doi_sang_thap_luc_phan(num)
input_str = str(num)
clean_str, invalid_chars = remove_invalid_chars(input_str)
base = get_base(clean_str)
base_10 = convert_to_base10(clean_str, base)

# In kết quả
print(f"Số {num} ở dạng nhị phân là: {binary}")
print(f"Số {num} ở dạng bát phân là: {octal}")
print(f"Số {num} ở dạng thập lục phân là: {hexadecimal}")
print(f"Số {num} sau khi loại bỏ các ký tự không hợp lệ là: {clean_str}")
print(f"Các ký tự không hợp lệ đã bị loại bỏ: {invalid_chars}")
print(f"Cơ số của chuỗi số {clean_str} là: {base}")
print(f"Chuỗi số {clean_str} ở dạng cơ số 10 là: {base_10}")
