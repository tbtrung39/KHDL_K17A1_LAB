while True:
    tu_so = int(input("Nhập tử số của phân số: "))
    mau_so = int(input("Nhập mẫu số của phân số: "))
    if mau_so == 0:
        print("Mẫu số không thể là 0. Vui lòng nhập lại.")
        continue
    else:
        print("Phân số đã nhập là:", tu_so, "/", mau_so)
        break