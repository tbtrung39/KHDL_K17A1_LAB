while True:
    tuso = int(input("Nhập tử số của phân số: "))
    mauso = int(input("Nhập mẫu số của phân số: "))
    if mauso != 0:
        break
    else:
        print("nhập lại")

print("Phân số vừa nhập là:", tuso, "/", mauso)
