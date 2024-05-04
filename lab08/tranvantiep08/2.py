def ucln(tu, mau):
    for i in range(min(tu, mau), 1, -1): 
        if tu % i == 0 and mau % i == 0 : 
            return i
    return 1

tuu = int(input('Nhap tu so : '))
mauu = int(input('Nhap mau so : '))
print('Phan so duoc rut gon la : ', tuu / ucln(tuu, mauu), '/', mauu / ucln(tuu, mauu))

