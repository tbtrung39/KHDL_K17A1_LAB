n = int(input("Nhập số lần tung xúc sắc: "))
xac_suat_3xx_khong_ra_6 = (5/6) ** 3
xac_suat_it_nhat_mot_lan = 1 - xac_suat_3xx_khong_ra_6
print("Xác suất có ít nhất một lần cả ba xúc sắc đều ra số 6 sau khi tung", n, "lần là:", round(xac_suat_it_nhat_mot_lan, 2))