from libs.xu_ly_thong_tin import nhapthongtinnv,inthongtin,sapxepthongtin
print("1.Nhập thông tin nhân viên mới")                                                   
print("2.In thông tin nhân viên ra màn hình")                                                    
print("3.Sắp xếp nhân viên giảm dần của thực lĩnh và in ra thông tin được sắp xếp")
select = int(input("Mời nhập lựa chọn của bạn: "))
if select == 1:
    nhapthongtinnv()
elif select == 2:
    inthongtin()
elif select == 3:
    sapxepthongtin()
else:
    print("Chức năng bạn vừa chọn không có trong MENU.")