def check_year(y):
    if y % 4 == 0 and ( y % 100 != 0 or y % 400 != 0):
        return True
    else:
        return False

def thang(t, y):
    if t <= 12 and t >= 1:
        if t == 4 or t == 6 or t == 9 or t == 11:
            return "30 ngày"
        elif t == 2:
            if check_year(y):
                return "29 ngày"
            else:
                return "28 ngày"
        else:
            print("31 ngày")

y = int(input("Năm: "))
year = check_year(y)
print(year)


t = int(input("Tháng: "))
Thang = thang(t,y)
print(Thang)