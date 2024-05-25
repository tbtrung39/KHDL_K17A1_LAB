Str=input("nhap chuoi tu ban phim: ")
dem =0
for i in Str:
    if 'a'<=i<='z' or "A"<=i<='Z' or '0'<=i<='9':
        continue
    else:
        dem+=1
print("so ky tu can tim la:", dem)