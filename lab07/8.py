#8
# cho arong
a=[]
so_nguyen=0
so_thuc=0
chuoi_ky_tu=0
# kiem tra
for phan_tu in a:
    if isinstance(phan_tu, int):
        so_nguyen+=1
    elif isinstance(phan_tu, float):
        so_thuc+=1
    elif isinstance(phan_tu, str):
        chuoi_ky_tu+=1
print("so nguyen cua tap hop a la:",so_nguyen)
print("so thuc cua tap hop a la:",so_thuc)
print("chuoi ky tu cua tap hop a la:",chuoi_ky_tu)