def ktra(y): 
    if y % 4 == 0 : 
        if y % 100 == 0 : 
            if y % 400 == 0 : 
                return True
            else: 
                return False
        else: 
            return False
    else: 
        return False
    
def so_ngay(y): 
    if ktra(y) : 
        return 366
    else: 
        return 365 
    
year = int(input('nhap nam : '))
if ktra(year):
    print(year, 'la nam nhuan ')
else: 
    print(year, 'la nam khong nhuan ')

print(f'so ngay trong nam {year} la : ', so_ngay(year))
