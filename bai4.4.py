tu_so=int(input("nhap tu so: "))
mau_so=False
while mau_so==False:
    mau_so=int(input("nhau mau so: "))
    if mau_so==0:
        print("nhap lai mau so")
    else:
        print("phan so co dang: ",tu_so,'/',mau_so)