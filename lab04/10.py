print("---------MENU---------")
print("------DRINK FRUIT------")
while True:
    print("---Chọn đồ uống---")
    print("   1. Cafe")
    print("   2. Cam vắt")
    print("   3. Nước ép carot")
    print("   4. Nước lọc")
    print("   5. Nước dừa")
    chon = int(input("Chọn nước uống mà bạn muốn mua (1-5): "))
    if chon == 1:
        print("Bạn đã chọn cafe")
    elif chon == 2:
        print("Bạn đã chọn Cam vắt")
    elif chon == 3:
        print("Bạn đã chọn nước ép Carot")
    elif chon == 4:
        print("Bạn đã chọn nước lọc")
    elif chon == 5:
        print("Bạn đã chọn nước dừa")
    elif chon==0:
        break
    else:
        print("Vui lòng nhập lại.")