print("Đổi giá trị thời gian")

giay = int(input("Nhập số giây: "))
phut = int(input("Nhập số phút: "))
gio = int(input("Nhập số giờ: "))
ngay = int(input("Nhập số ngày: "))

sum_giay = ngay * 24 * 3600 + gio * 3600 + phut * 60 + giay
print(f"{ngay} ngày, {gio} giờ, {phut} phút, {giay} giây tương ứng là {sum_giay} giây.")
