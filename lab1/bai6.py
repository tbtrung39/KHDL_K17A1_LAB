
time_use = int(input("Nhập thời gian sử dụng bóng đèn (giây): "))
a = 7000
b = (220 * 2.7 * time_use) / (1000 * 3600)
_money = b * a
print("Tiền điện phải trả:", round(_money, 2), "VNĐ")

