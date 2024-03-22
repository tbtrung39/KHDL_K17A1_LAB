#câu 2
#a) tổng của chuỗi đan dấu
so = 1
tong = 0
dau = 1
while True:
    so += 1
    dau *= -1
    tong += dau * 1/so
    print(f"tổng của chuỗi đan dấu là{tong}")
    break
#b) tổng của chuỗi
so_nhan = 1
tong = 0
so = 1
while True:
    if so_nhan >1 and so >0:
        so_nhan += 1
        so += 1
        tong += 1/2 + 1/so_nhan*so
        print(f"tổng của chuỗi vô tận là:{tong}")
    else:
        print("vui lòng nhập số lớn hơn 0")
        break
#c)tổng chuỗi 
so = 1
tong = 0
while True:
    so += 1
    tong += 1/so**0.5
    print(f"tổng của chuỗi đan dấu là{tong}")
    break
