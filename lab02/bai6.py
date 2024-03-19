n=int(input("nhập số nguyên co 3 chữ số: "))
hang_tram= n//100
hang_chuc=(n%100)//10
hang_dv= n%10
if hang_tram==1:
    print("một trăm", end=" ")
elif hang_tram==2:
    print("hai trăm", end=" ")
elif hang_tram==3:
    print("ba trăm", end=" ")
elif hang_tram==4:
    print("bốn trăm", end=" ")
elif hang_tram==5:
    print("năm trăm", end=" ")
elif hang_tram==6:
    print("sáu trăm", end=" ")
elif hang_tram==7:
    print("bảy trăm", end=" ")
elif hang_tram==8:
    print("tám trăm", end=" ")
elif hang_tram==9:
    print("chín trăm", end=" ")
else:
    print("không hợp lệ!!!")

if hang_chuc==0 and hang_dv!=0:
    print("linh", end=" ")
elif hang_chuc==1:
    print('mười', end=" ")
elif hang_chuc ==2:
    print("hai mươi", end=" ")
elif hang_chuc ==3:
    print("ba mươi", end=" ")
elif hang_chuc ==4:
    print("bốn mươi", end=" ")
elif hang_chuc ==5:
    print("năm mươi", end=" ")
elif hang_chuc ==6:
    print("sáu mươi", end=" ")
elif hang_chuc ==7:
    print("bảy mươi", end=" ")
elif hang_chuc ==8:
    print("tám mươi", end=" ")
elif hang_chuc ==9:
    print("chín mươi", end=" ")
elif hang_chuc<0 and hang_chuc>=10:
    print("số không hợp lệ!!!")

if hang_dv==0:
    print("")
elif hang_dv==1:
    print("một")
elif hang_dv==2:
    print("hai")
elif hang_dv==3:
    print("ba")
elif hang_dv==4:
    print("bốn")
elif hang_dv==5:
    print("năm")
elif hang_dv==6:
    print("sáu")
elif hang_dv==7:
    print("bảy")
elif hang_dv==8:
    print("tám")
elif hang_dv==9:
    print("chín")
elif hang_dv<0 and hang_dv>=10:
    print("số không hợp lệ!!!")