# nhap TU BAN PHIM MOT CHUOI
str=input("moi nhap chuoi")
print("chuoi duoc in ra la",str)
dem=0
for c in str:
    if "0"<=c<="9":
        dem+=1
print("so ky tu la chuoi trong day vua nhap la:",dem)