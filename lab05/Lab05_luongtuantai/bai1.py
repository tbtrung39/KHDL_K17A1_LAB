str=input("nhap chuoi tu ban phim: ")
dem=0
for i in str:
    if '0'<=i<='9':
        dem+=1
print("so cac ky tu la so trong chuoi da nhap la:", dem)