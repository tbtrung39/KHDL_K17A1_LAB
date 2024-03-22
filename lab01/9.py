n=int(input("Nhập số lần tung xúc sắc :"))
so_lan_tung_ca_3_khong_ra_6=(5/6)**n
so_lan_tung_ca_3_ra_6=1-so_lan_tung_ca_3_khong_ra_6
print(f'Xác suất tung 3 xúc sắc ra số 6 qua {n} lần là {so_lan_tung_ca_3_ra_6:.2f}')