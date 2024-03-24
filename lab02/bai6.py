abc = int(input("Nhập vào một số nguyên có ba chữ số: "))
if 100 <= abc <= 999:
    print("Cách đọc của số nguyên", abc, "là:")
    tram = abc // 100
    chuc = (abc % 100) // 10
    donvi = abc % 10


    if tram != 0:
        if tram == 1:
            print("một trăm", end=" ")
        elif tram == 2:
            print("hai trăm", end=" ")
        elif tram == 3:
            print("ba trăm", end=" ")
        elif tram == 4:
            print("bốn trăm", end=" ")
        elif tram == 5:
            print("năm trăm", end=" ")
        elif tram == 6:
            print("sáu trăm", end=" ")
        elif tram == 7:
            print("bảy trăm", end=" ")
        elif tram == 8:
            print("tám trăm", end=" ")
        elif tram == 9:
            print("chín trăm", end=" ")
    
    if chuc != 0:
        if chuc == 1:
            print("mười", end=" ")
        elif chuc == 2:
            print("hai mươi", end=" ")
        elif chuc == 3:
            print("ba mươi", end=" ")
        elif chuc == 4:
            print("bốn mươi", end=" ")
        elif chuc == 5:
            print("năm mươi", end=" ")
        elif chuc == 6:
            print("sáu mươi", end=" ")
        elif chuc == 7:
            print("bảy mươi", end=" ")
        elif chuc == 8:
            print("tám mươi", end=" ")
        elif chuc == 9:
            print("chín mươi", end=" ")

    if donvi != 0 and chuc != 0:
        if donvi == 1:
            print("một", end=" ")
        elif donvi == 2:
            print("hai", end=" ")
        elif donvi == 3:
            print("ba", end=" ")
        elif donvi == 4:
            print("bốn", end=" ")
        elif donvi == 5:
            print("năm", end=" ")
        elif donvi == 6:
            print("sáu", end=" ")
        elif donvi == 7:
            print("bảy", end=" ")
        elif donvi == 8:
            print("tám", end=" ")
        elif donvi == 9:
            print("chín", end=" ")
    if donvi != 0 and chuc == 0:
        if donvi == 1:
            print("linh một",end=" ")
        elif donvi == 2:
            print("linh hai",end=" " )
        elif donvi == 3:
            print("linh ba",end=" ")
        elif donvi == 4:
            print("linh bốn",end=" ")
        elif donvi == 5:
            print("linh năm",end=" ")
        elif donvi == 6:
            print("linh sáu",end=" ")
        elif donvi == 7:
            print("linh bảy",end=" ")
        elif donvi == 8:
            print("linh tám",end=" ")
        elif donvi == 9:
            print("linh chín",end=" ")      
else:
    print("Số bạn nhập không phải là số nguyên có ba chữ số.")