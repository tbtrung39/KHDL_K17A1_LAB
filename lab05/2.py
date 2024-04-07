n= input('Nhap tu ban phim:')
so_dem=0
for kiem_tra in n:
    if not kiem_tra.isdigit() and not kiem_tra.isalpha():
        so_dem+=1
print("So luong khong phai ky tu tieng anh va khong phai so trong chuoi la:",so_dem)