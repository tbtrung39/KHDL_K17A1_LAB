str=input("nhap chuoi ki tu:")
print("chuoi ki tu da nhap:",str)
dem=0
for c in str:
    if "0"<=c<="9":
        dem+=1
print("so cac ki tu la so trong chuoi:",dem)