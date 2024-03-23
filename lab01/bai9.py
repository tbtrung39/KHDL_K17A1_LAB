n = int(input("Nhập số lần tung xúc sắc (n): "))

# Xác suất không có lần nào cả ba xúc sắc đều ra mặt 6
xac_suat_khong_ra_6 = (5 / 6) ** n

# Xác suất ít nhất có một lần cả ba xúc sắc đều ra mặt 6
xac_suat = 1 - xac_suat_khong_ra_6

print("Xác suất ít nhất có một lần cả ba xúc sắc đều ra mặt 6 sau", n, "lần tung là:", round(xac_suat, 2))
