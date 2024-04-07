
Str = input("Nhập chuỗi: ")
charhex = set("0123456789ABCDEF")
kiemtraloi = set(Str) - charhex
if kiemtraloi:
    kytukhonghople = ''.join(char for char in Str if char in charhex)
    print("Chuỗi đã được làm sạch:", kytukhonghople)
    sothapphan = int(kytukhonghople, 16)
    print("Giá trị thập phân của chuỗi:", sothapphan)
else:
    print("Chuỗi là chuỗi hệ Hex.")
