ky_tu = input("Nhập một ký tự: ")
if len(ky_tu) > 0:
    gia_tri_ascii = ord(ky_tu[0])
    print("Giá trị ASCII của ký tự", ky_tu, "là:", gia_tri_ascii)
else:
    print("Không có ký tự nào được nhập.")