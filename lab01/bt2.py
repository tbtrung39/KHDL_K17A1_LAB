d = int(input("nhập vào số ngày: "))
h = int(input("nhập vào số giờ: "))
m = int(input("nhập vào số phút: "))
s = int(input("nhập vào số giây: "))
ds= d * 86400 
hs = h *3600
ms = m * 60
print(f"thời gian sau khi quy đổi ra giây {d} ngày = {ds}s, {h} giờ = {hs}s , {m} phút = {ms}s")