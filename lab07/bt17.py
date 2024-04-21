n = int(input("Số lượng: "))
thong_tin_sv = {}
for i in range(n):
    ma_sv = input("Mã sinh viên: ")
    ten_sv = input("Tên : ")
    diem_sv = float(input("Điểm: "))
    lam_tron_diem = max(0, min(10, round(diem_sv))) 
    thong_tin_sv[ma_sv] = {"Name": ten_sv, "Score": lam_tron_diem}
diem_giam_dan = sorted(thong_tin_sv.items(), key=lambda x: x[1]["Score"], reverse=True)
print("Danh sách sinh viên theo điểm giảm dần:")
for ma_sv, info in diem_giam_dan:
    print("Mã sinh viên: ",ma_sv)
    print("Tên sinh viên: ",info["Name"])
    print("Điểm số:", info["Score"])
    print()