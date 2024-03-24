tg1 = int(input("Gio bat dau: "))
tg2 = int(input("gio ket thuc: "))

tg=tg2-tg1

if tg<0:
    print("Nhap vao khong hop le")
elif tg1<5 or tg2>22:
    print("Quan da dong.")
else:
    if tg1>=11 and tg2<=15:
        if tg<=3:
            hoa_don= 100000*tg*0.9
            print(f"Hoa don la:{hoa_don}")
        else:
            hoa_don = (100000*3+ 100000*(tg-3)*0.75)*0.9
            print(f"Hoa don la:{hoa_don}")
    elif tg<=3:
        hoa_don= 100000*tg
        print(f"Hoa don la:{hoa_don}")
    else:
        hoa_don = 100000*3+ 100000*(tg-3)*0.75
        print(f"Hoa don la:{hoa_don}")