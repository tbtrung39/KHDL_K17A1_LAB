from package import doicoso_2
a = input("Chuỗi kí tự cần lọc là: ")
print(doicoso_2.loai_ki_tu(a))

b = input("Nhập số ở hệ nhị phân: ")
print(doicoso_2.he2_sang_he10(b))

c = input("Nhập số ở hệ bát phân: ")
print(doicoso_2.he8_sang_he10(c))

d = input("Nhập số ở hệ thập lục phân: ")
print(doicoso_2.he16_sang_he10(d))