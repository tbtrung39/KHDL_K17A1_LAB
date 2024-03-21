d = int(input("Nhập vào số ngày: "))
h = int(input("Nhập vào số giờ: "))
m = int(input("Nhập vào số phút: "))
s = int(input("Nhập vào số giây: "))
ds= d * 86400 
hs = h *3600
ms = m * 60
print(f"Thời gian sau khi quy đổi ra giây {d} ngày = {ds}s, {h} giờ = {hs}s , {m} phút = {ms}s")