chuoi = input("nhập vào chuỗi kí tự:")
so_ki_tu_ko_phai_tieng_anh_va_so = 0
for i in chuoi:
    if not i.isalpha() and not i.isdigit():
        so_ki_tu_ko_phai_tieng_anh_va_so += 1
print(f"số kí tự không phải là chữ cái tiếng anh và số là: {so_ki_tu_ko_phai_tieng_anh_va_so}")