chieu_cao = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150,
             142, 148, 165, 170, 178, 156, 145,
             149, 163, 162, 159, 165, 165, 170, 180, 155, 159,
             155, 153, 152, 180, 168, 169, 168, 167, 170]
tong_sv = len(chieu_cao)
print("Tong so sinh vien la: ", tong_sv, "sinh vien")
chieu_cao_tb = sum(chieu_cao)/tong_sv
print("Chieu cao trung binh cua cac sinh vien trong nhom la: ", chieu_cao_tb)
chieu_cao_khac_nhau = set(chieu_cao)
so_luong = len(chieu_cao_khac_nhau)
print("So luong chieu cao khac nhau la: ", so_luong)
tb_chieu_cao_khac_nhau = sum(chieu_cao_khac_nhau)/so_luong
print("Chieu cao trung binh cua nhom moi la: ", tb_chieu_cao_khac_nhau)