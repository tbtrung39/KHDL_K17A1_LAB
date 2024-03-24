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
        break
    elif chon == 2:
        print("Bạn đã chọn cam vắt")
        break
    elif chon == 3:
        print("Bạn đã chọn nước ép carot")
        break
    elif chon == 4:
        print("Bạn đã chọn nước lọc")
        break
    elif chon == 5:
        print("Bạn đã chọn nước dừa")
        break
    else:
        print("Bạn đã nhập sai nội dung. Vui lòng nhập lại.")