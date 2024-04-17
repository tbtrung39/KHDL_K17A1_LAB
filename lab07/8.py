A = {1, 2.5, "hello", 3, 4.8, "world", 5, 6, "python"}
#dem so phan tu la so nguyen, so thuc va chuoi ky tu cua tap hop A
so_luong_so_nguyen = sum(isinstance(x, int) for x in A)
so_luong_ket_thuc = sum(isinstance(x, float) for x in A)
so_luong_chuoi = sum(isinstance(x, str) for x in A)
# in ket qua
print("so phan tu la so nguyen trong tap hop A:",so_luong_so_nguyen)
print("so phan tu la so thuc trong tap hop A:",so_luong_ket_thuc)
print("so phan tu la chuoi ky tu trong tap hop A:",so_luong_chuoi)
