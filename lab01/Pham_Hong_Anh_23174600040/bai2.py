print("2. Đổi giá trị thời gian")
s = int(input("Nhập số giây: "))
m = int(input("Nhập số phút: "))
h = int(input("Nhập số giờ: "))
d = int(input("Nhập số ngày: "))

sum_s = d * 24 * 3600 + h * 3600 + m * 60 + s
print(f"{d} ngày, {h} giờ, {m} phút, {s} giây tương ứng là {sum_s} giây.")
