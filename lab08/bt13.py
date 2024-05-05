def namnhuan(year):
    if (year%4 == 0 and year %100!=0) or (year%400==0):
        return f"{year} la nam nhuan"
    return f"{year} khong la nam nhuan"
year = int(input("nhap nam:"))
print(namnhuan(year))
