str=input("Nhap ki tu chuoi:")
dem=0 
for c in str:
    if not c.isalpha() and not c.isdigit():
        dem+=1
print("so ki tu khong phai tieng anh va khong phai so:",dem)