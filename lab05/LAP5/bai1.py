n=input('Nhap vao ban phim:')
so_dem=0
for so in n:
    if so.isdigit():
        so_dem+=1
print("Số ký tự là số trong chuỗi là:",so_dem)