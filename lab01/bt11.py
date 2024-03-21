n = int(input("Nhập số lần tung xúc sắc: "))
ti_le = (1/6)**3
khong_xay_ra = (1-ti_le)**n
xs = 1 - khong_xay_ra
print("Xác suất: ", round(xs,2))