so_kw=float(input("Nhập số kw:"))
if so_kw<=100 and so_kw>0:
    tien_dien=so_kw*2000
elif so_kw<=200:
    tien_dien=(100*2000 + (so_kw-100)*2500)
elif so_kw<=300:
    tien_dien=(100*2000 + 100*2500 + (so_kw-200)*3000)
elif so_kw>300:
    tien_dien=(100*2000 + 100*2500 + 100*3000 + (so_kw-300)*5000)
print("Cái giá phải trả:",tien_dien)