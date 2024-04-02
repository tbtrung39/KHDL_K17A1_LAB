nhap = input("Nhập một ký tự: ")
if len(nhap) > 0:
    gia_tri_ascii = ord(nhap[0])
    print("Giá trị ASCII của ký tự", nhap, "là:", gia_tri_ascii)
else:
    print("Không có ký tự nào được nhập.")