n = int(input("số lượng: "))
thong_tin_sv = {}
for i in range(n):
    ma_sv = input("mã sinh viên: ")
    ten_sv = input(" tên : ")
    diem_sv = float(input(" điểm: "))
    lam_tron_diem = max(0, min(10, round(diem_sv))) 
    thong_tin_sv[ma_sv] = {"name": ten_sv, "score": lam_tron_diem}
diem_giam_dan = sorted(thong_tin_sv.items(), key=lambda x: x[1]["score"], reverse=True)
print("Danh sách sinh viên theo điểm giảm dần:")
for ma_sv, info in diem_giam_dan:
    print("Mã sinh viên:", ma_sv)
    print("Tên sinh viên:", info["name"])
    print("Điểm số:", info["score"])
    print()