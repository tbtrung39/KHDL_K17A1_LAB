x1 = int(input("nhap toa do diem x cua dinh A: "))
y1 = int(input("nhap toa do diem y cua dinh A: "))
x2 = int(input("nhap toa do diem x cua dinh B: "))
y2 = int(input("nhap toa do diem y cua dinh B: "))
x3 = int(input("nhap toa do diem x cua dinh C: "))
y3 = int(input("nhap toa do diem y cua dinh C: "))
toa_do_x_trong_tam = (x1+x2+x3)/3
print(toa_do_x_trong_tam)
toa_do_y_trong_tam = (y1+y2+y3)/3
print(toa_do_y_trong_tam)
toa_do_x_trong_tam = round(toa_do_x_trong_tam, 2)
toa_do_y_trong_tam = round(toa_do_y_trong_tam, 2)
trong_tam = (toa_do_x_trong_tam, toa_do_y_trong_tam)
print('toa do trong tam la: ', trong_tam)