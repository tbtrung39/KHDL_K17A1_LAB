A = set(input("Nhap cac phan tu cua tap hop A, cach nhau bang dau phay: ").split(','))
so_nguyen = 0
so_thuc = 0
chuoi = 0
for phan_tu in A:
    if phan_tu.isdigit():
        so_nguyen += 1
    elif '.' in phan_tu:
        float(phan_tu)
        so_thuc += 1
        chuoi += 1
    else:
        chuoi += 1
print(f"So phan tu so nguen trong tap hop A: {so_nguyen}")
print(f"So phan tu so thuc trong tap hop A: {so_thuc}")
print(f"So phan tu chuoi trong tap hop A: {chuoi}")
