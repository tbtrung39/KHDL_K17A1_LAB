ban_kinh = int(input("Nhap ban kinh: "))
chieu_cao = int(input("Nhap chieu cao: "))
s_xq_ktru = ban_kinh * chieu_cao * 3.14
s_tp_ktru = 3.14 * ban_kinh**2 + 2 * 3.14 * ban_kinh * chieu_cao
the_tich_ktru = 3.14 * ban_kinh**2 * chieu_cao
print("Dien tich xung quanh khoi tru: ", s_xq_ktru)
print("Dien tich toan phan khoi tru: ", s_tp_ktru)
print("The tich khoi tru: ",the_tich_ktru)