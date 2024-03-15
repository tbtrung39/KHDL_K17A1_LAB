ban_kinh = int(input("nhập bán kính: "))
chieu_cao = int(input("nhập chiều cao: "))
dien_tich_xung_quanh = 3.14 * ban_kinh * chieu_cao
dien_tich_toan_phan = 3.14 * ban_kinh * chieu_cao + 3.14 * ban_kinh ** 2
the_tich = 3.14 * ban_kinh ** 2 * chieu_cao
print("dtxq", dien_tich_xung_quanh)
print("dttp", dien_tich_toan_phan)
print("v", the_tich)