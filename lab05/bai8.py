str=input("nhap mot chuoi: ")
tu_don=input("nhap mot tu don: ")
x=str.split()
dem=0
for i in x:
    if i == tu_don:
        dem+=1
print("so tu don can tim la:", dem)