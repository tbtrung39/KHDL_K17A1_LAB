str = input("Nhap chuoi ki tu: ")
print("Chuoi li tu via nhap: ",str)
dem = 0 
for c in str:
    if "0"<=c <="9":
        dem += 1
print("So cac ki tu la so trong chuoi da nhap =", dem)