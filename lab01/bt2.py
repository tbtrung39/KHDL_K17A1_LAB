s = int(input("Nhập số giây: "))
d = s // (24 * 3600)
s = s % (24 * 3600)
h = s // 3600
s %= 3600
m = s // 60
s %= 60
print(f"{d} ngày, {h} giờ, {m} phút, {s} giây")