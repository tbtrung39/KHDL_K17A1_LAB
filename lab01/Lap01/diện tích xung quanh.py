r=float(input('Nhap ban kinh: '))
h=float(input('Nhap chieu cao: '))
sxq=2*3.14*r*h
dien_tich_toan_phan=sxq+2*3.14*r**2
the_tich=3.14*r**2*h
print(f'Dien tich xung quanh khoi tru la {sxq:.2f}')
print(f'Dien tich toan phan khoi tru la {dien_tich_toan_phan:.2f}')
print(f'The tich khoi tru la {the_tich:.2f}')