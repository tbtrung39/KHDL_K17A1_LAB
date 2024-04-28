def coban(a,b):
    cong = a + b
    tru = a -b
    nhan = a * b
    chia = a / b
    return cong, tru , nhan , chia

a = int(input("A: "))
b = int(input("B;"))
COban = coban(a,b)    
print("Cộng Trừ Nhân Chia lần lượt: ",COban)