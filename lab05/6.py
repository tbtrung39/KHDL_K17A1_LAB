str = input("Nhập chuỗi: ")
hex = all(c in "0123456789abcdefABCDEF" for c in str)
if hex:
    print("Chuỗi đã nhập là chuỗi hex.")
    thap_phan = int(str, 16)
    print("Giá trị thập phân tương ứng:", thap_phan)
else:
    print("Chuỗi đã nhập không phải là chuỗi hex.")
    str_loai_bo = ''.join(c for c in str if c.isdigit() or c.lower() in 'abcdef')
    print("Chuỗi sau khi loại bỏ ký tự không phải hex:", str_loai_bo)
    thap_phan = int(str_loai_bo, 16)
    print("Giá trị thập phân tương ứng:", thap_phan)
