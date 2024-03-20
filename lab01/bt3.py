ban_kinh = int(input("Nhập bán kính: "))
chieu_cao = int(input("Nhập chiều cao: "))
s_xq_ktru = ban_kinh * chieu_cao * 3.14
s_tp_ktru = 3.14 * ban_kinh**2 + 2 * 3.14 * ban_kinh * chieu_cao
the_tich_ktru = 3.14 * ban_kinh**2 * chieu_cao
print("Diện tích xung quanh khối trụ: ", s_xq_ktru)
print("Diện tích toàn phần khối trụ: ", s_tp_ktru)
print("Thể tích khối trụ: ",the_tich_ktru)