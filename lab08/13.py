y = int(input("Năm::"))

def kiem_tra(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 != 0):
        return True
    else:
        return False

m = int(input("Tháng:"))    
def thang( m , y):
    if m >= 1 and m <= 12:
        if m == 4 or m == 6 or m == 9 or m == 11:
            return "30 ngày"
        elif m == 2 :
            if kiem_tra(y):
                return "29 ngày"
            else:
                return "28 ngày"
        else:
            return "31 ngày"
        
năm = kiem_tra(y)
print(năm)


tháng = thang(m,y)
print(tháng)