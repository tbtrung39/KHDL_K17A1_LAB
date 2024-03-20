#Viết chương trình vẽ hình chữ nhật và điền dấu * như hình sau:
chieu_dai=int(input("moi nhap chieu dai:"))
chieu_rong=int(input("moi nhap chieu rong:"))
for i in range(chieu_dai):
    for j in range(chieu_rong):
        print("*",end="")
    print()