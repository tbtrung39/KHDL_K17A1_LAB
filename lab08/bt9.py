def phep_tinh(a,b):
    cong = a + b
    tru = a - b
    nhan = a * b
    chia = a / b
    return cong, tru , nhan , chia
a = int(input("A: "))
b = int(input("B: "))
ket_qua = phep_tinh(a,b)    
print(f"Phép Cộng Trừ Nhân Chia lần lượt {ket_qua}")