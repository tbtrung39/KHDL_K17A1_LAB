import pk8 as b8




n = int(input("Nhập kích thước của ma trận vuông: "))




ma_tran = b8.nhap_ma_tran(n)

b8.in_ma_tran(ma_tran)

print("Ma trận chuyển vị là:")

b8.in_ma_tran(b8.ma_tran_chuyen_vi(ma_tran))




if b8.kiem_tra_ma_tran_doi_xung(ma_tran):

    print("Ma trận là ma trận đối xứng.")

else:

    print("Ma trận không phải là ma trận đối xứng.")