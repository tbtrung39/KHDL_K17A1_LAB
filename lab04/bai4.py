tu_so = int(input("Nhap tu so la:"))
while True:
    mau_so = int(input("Nhap mau so la:"))
    if mau_so == 0:
        print("Moi nhap lai !!!")
    if mau_so != 0:
        print("Phan so vua nhap tu ban phim la:",tu_so,"/",mau_so)
        break
