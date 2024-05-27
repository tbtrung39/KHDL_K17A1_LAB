from package import in_ra,cs01,cs8p,cs16p
from package import xoa_kt_ko_hop_le,cs2_to_cs10,cs8_to_cs10
n = int(input("nhập vào số nguyên n: "))
in_ra(n)
print(f"n sau khi chuyển qua hệ nhị phân là: {cs01(n)}")
print(f"n sau khi chuyển qua hệ bát phân là: {cs8p(n)}")
print(f"n sau khi chuyển qua hệ thập lục phân là: {cs16p(n)}")

chuoi = input("nhập vào chuỗi: ")
cs2 = input("nhập vào chuỗi: ")
cs10 = input("nhập vào chuỗi: ")
print(f"chuỗi n sau khi xóa ký tự không hợp lệ: {xoa_kt_ko_hop_le(chuoi)}")
print(f"chuỗi n sau khi chuyển từ cơ số 2 qua cơ số 10 là {cs2_to_cs10(cs2)}")
print(f"chuỗi n sau khi chuyển từ cơ số 2 qua cơ số 10 là {cs8_to_cs10(cs10)}")