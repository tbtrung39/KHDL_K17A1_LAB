import math
van_toc_ban_dau = float(input("Nhập vào vận tốc ban đầu:"))
a = float(input("Nhập vào vận tốc ô tô đang chạy:"))
#Vận tốc ban đầu của v0 là t=0
v0=0*math.log(5,4)+a**4
#Thời gian ô tô đi được cho đến lúc dừng là
time=v0/a
print(f"Thời gian ô tô đi được cho đên lúc dừng {time}")