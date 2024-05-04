def pheptinh(a, b): 
    cong = a + b 
    tru = a - b 
    nhan = a * b 
    chia = a / b 
    return cong, tru, nhan, chia

c = int(input('nhap so dau : '))
d = int(input('nhap so thu hai : '))
print('cac phep tinh toan hoc (cong, tru, nhan, chia) la : ', pheptinh(c, d))