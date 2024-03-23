n = int(input("Nhập vào một số nguyên có ba chữ số: "))

if n < 100 or n > 999:
    print("Số vừa nhập không có ba chữ số.")
else:
    hang_tram = n // 100
    hang_chuc = (n % 100) // 10
    hang_don_vi = n % 10

    if hang_tram == 1:
        print("Một trăm", end=" ")
    elif hang_tram == 2:
        print("Hai trăm", end=" ")
    elif hang_tram == 3:
        print("Ba trăm", end=" ")
    elif hang_tram == 4:
        print("Bốn trăm", end=" ")
    elif hang_tram == 5:
        print("Năm trăm", end=" ")
    elif hang_tram == 6:
        print("Sáu trăm", end=" ")
    elif hang_tram == 7:
        print("Bảy trăm", end=" ")
    elif hang_tram == 8:
        print("Tám trăm", end=" ")
    elif hang_tram == 9:
        print("Chín trăm", end=" ")

    if hang_chuc == 1:
        if hang_don_vi == 0:
            print("mười")
        elif hang_don_vi == 1:
            print("mười một")
        elif hang_don_vi == 2:
            print("mười hai")
        elif hang_don_vi == 3:
            print("mười ba")
        elif hang_don_vi == 4:
            print("mười bốn")
        elif hang_don_vi == 5:
            print("mười năm")
        elif hang_don_vi == 6:
            print("mười sáu")
        elif hang_don_vi == 7:
            print("mười bảy")
        elif hang_don_vi == 8:
            print("mười tám")
        elif hang_don_vi == 9:
            print("mười chín")
    else:
        if hang_chuc == 2:
            print("hai mươi", end=" ")
        elif hang_chuc == 3:
            print("ba mươi", end=" ")
        elif hang_chuc == 4:
            print("bốn mươi", end=" ")
        elif hang_chuc == 5:
            print("năm mươi", end=" ")
        elif hang_chuc == 6:
            print("sáu mươi", end=" ")
        elif hang_chuc == 7:
            print("bảy mươi", end=" ")
        elif hang_chuc == 8:
            print("tám mươi", end=" ")
        elif hang_chuc == 9:
            print("chín mươi", end=" ")

        if hang_don_vi == 1:
            print("một")
        elif hang_don_vi == 2:
            print("hai")
        elif hang_don_vi == 3:
            print("ba")
        elif hang_don_vi == 4:
            print("bốn")
        elif hang_don_vi == 5:
            print("năm")
        elif hang_don_vi == 6:
            print("sáu")
        elif hang_don_vi == 7:
            print("bảy")
        elif hang_don_vi == 8:
            print("tám")
        elif hang_don_vi == 9:
            print("chín")