def name(): 
    hoten = input('nhap ho va ten : ')
    return hoten

def hometown(): 
    quequan = input('nhap que quan : ')
    return quequan

def tn_ct():
    thamnien_ct = float(input('nhap tham nien cong tac : '))
    return thamnien_ct

def salary(n):
    if n > 3 and n < 10 : 
        return 6000000
    elif n >= 10 : 
        return 15000000
    return 0

def xuat() : 
    return name(), hometown(), tn_ct(), salary(tn_ct())

print(xuat())