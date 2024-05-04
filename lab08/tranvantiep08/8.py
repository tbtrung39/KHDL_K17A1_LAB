def sodo_circle(r): 
    chuvi = 2 * r * 3.14
    dientich = r ** 2 * 3.14
    return chuvi, dientich

r = float(input('nhap ban kinh duong tron : '))
print('(chuvi, dientich) ma hinh tron co duoc la : ', sodo_circle(r))