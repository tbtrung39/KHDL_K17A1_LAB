Str = input("Nhập chuỗi ký tự: ")
Str = Str.upper()
a = set('0123456789ABCDEF')
b = ''
for char in Str:
    if char in a:
        b += char
c = int(b, 16)
print("Chuỗi sau khi loại bỏ các ký tự không thuộc hệ Hex và chuyển sang số thập phân:", c)
