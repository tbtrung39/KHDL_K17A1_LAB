chieu_dai = int(input("Nhập chiều dài của hình chữ nhật là:"))
chieu_rong = int(input("Nhập chiều rộng của hình chữ nhật là:"))
for i in range(chieu_rong):
    for j in range(chieu_dai):
        print("*", end ='')
    print("\r")