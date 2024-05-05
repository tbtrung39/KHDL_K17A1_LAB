def nam_nhuan(y):
    flag = True
    if y%100 !=0 and y%4 ==0 or y%400 == 0:
        return flag
    flag = False

def xac_dinh_ngay(thang,nam):
    if thang < 1 or thang > 12:
        print("vui long nhap thang tu 1 den 12")        
    if thang ==1 or thang == 3 or thang ==5 or thang ==7 or thang ==8 or thang == 10 or thang ==12:
        so_ngay = 31
    elif thang ==4 or thang ==6 or thang ==9 or thang ==11:
        so_ngay= 30
    elif thang ==2:
        if nam_nhuan(nam):
            so_ngay = 29
            return so_ngay
        so_ngay = 28
    return so_ngay
    
month = int(input("nhap thang (1 -> 12):"))
year = int(input("nhap so nam: "))
print("so ngay toi da cua thang",month,"trong nam",year,"la",xac_dinh_ngay(month,year))    