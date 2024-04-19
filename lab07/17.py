so_luong_sv = int(input("Nhap so luong sinh vien la: "))
tu_dien_sv = {}
for i in range(1, so_luong_sv+1):
    msv =int(input("Nhap ma sinh vien gom 6 so la: "))
    ten_sv =input("Nhap ten sinh vien la: ")
    diem_so = round(float(input("Nhap diem so cua sinh vien do la: ")))
    tu_dien_sv[msv] = {'Ten':ten_sv, 'Diem':diem_so}
sap_xep = sorted(tu_dien_sv.items(),key=lambda x: x[1]['Diem'],reverse=True)
print("\nDanh sach sinh vien theo diem so giam dan la: ")
for msv, tu_dien in sap_xep:
    print(f"Ma sv:{msv}, Ten sv:{tu_dien['Ten']}, Diem:{tu_dien['Diem']}")