n = int(input("Nhập kích thước ma trận vuông: "))

from package import matranvuong

print("1. Ma trận vuông.")
tao_ma_tran = matranvuong.Ma_tran_vuong(n)
for row in tao_ma_tran:
    print(row)

print("2. Tính ma trận chuyển vị")
ma_tran_chuyen_vi = matranvuong.Ma_tran_chuyen_vi(tao_ma_tran)
for row in ma_tran_chuyen_vi:
    print(row)

print("3. Kiểm tra ma trận đối xứng")
ma_tran_doi_xung = matranvuong.doi_xung(tao_ma_tran)
if ma_tran_doi_xung:
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")