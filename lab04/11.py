# 11. Viết chương trình gọi đồ uống. Giả sử menu của chúng ta có các loại thức uống như sau
while True:
    a=int(input("moi nhap do uong:"))
    if a==1:
        print("cafe")
    elif a==2:
        print("cam vat")
    elif a==3:
        print("nuoc ep ca rot")
    elif a==4:
        print("nuoc loc")
    elif a==5:
        print("nuoc dua")
    else:
        break
    print("1.caphe",a==1)
    print("2.cam vat",a==2)
    print("3.nuoc ep ca rot",a==3)
    print("4.nuoc loc",a==4)
    print("5.nuoc dua",a==5)
