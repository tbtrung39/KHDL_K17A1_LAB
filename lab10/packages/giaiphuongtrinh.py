def phuong_trinh_bac1(a, b):
    return -b/a
def phuong_trinh_bac2(a, b, c):
    delta = b**2 - 4*a*c
    if delta<0:
        return 'Phuong trinh vo nghiem'
    elif delta==0:
        return ' Phuong trinh co 1 nghiem kep la: {-b/(2*a)}'
    else:
        return 'Phuong trinh co hai nghiem phan biet la: {(-b+delta**0.5)/(2*a)} va {(-b-delta**0.5)/(2*a)}'     
    