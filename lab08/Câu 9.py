def phep_tinh(a,b):
    cong = a + b
    tru = a - b
    chia = a / b
    nhan = a * b
    return cong,tru,chia,nhan
a = int(input("Nhập số: "))
b = int(input("Nhập số: "))
cong,tru,chia,nhan=phep_tinh(a,b)
print("Tổng là: ",cong)
print("Hiệu là: ",tru)
print("Thương là: ",chia)
print("Tích là:  ",nhan)