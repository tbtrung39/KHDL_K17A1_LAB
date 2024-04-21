chieu_cao_sv = [161,182,161,154,176,171,170,174,150,142,148,165,170,180,155,159,155,153,152,162,180,168,169,168,167,170]
so_luong_sv = len(chieu_cao_sv)
chieu_cao_tb = sum(chieu_cao_sv)/so_luong_sv
print("Tong so luong sinh vien la:",so_luong_sv)
print("Chieu cao trung binh cua cac sinh vien trong nhom la:",chieu_cao_tb)
thong_ke_chieu_cao = {}
for chieu_cao in chieu_cao_sv:
    thong_ke_chieu_cao[chieu_cao]=thong_ke_chieu_cao.get(chieu_cao,0)+1
tong_chieu_cao = sum(thong_ke_chieu_cao)
so_luong_chieu_cao_khacnhau = len(chieu_cao_sv)
chieu_cao_tb = tong_chieu_cao/len(chieu_cao_sv)
chieu_cao_tb = round(chieu_cao_tb,2)
for chieu_cao in thong_ke_chieu_cao:
    print(chieu_cao)
print("Chieu cao trung binh cua nhom la:",chieu_cao_tb)