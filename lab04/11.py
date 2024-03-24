menu   =  {1 : 'Cafe',2 : 'Cam vắt ',3 :'Nước ép cà rốt ',4:'Nước lọc',5:'Nước dừa'}


while True:
    print('menu của bạn ở đây : ','\n')
    for i in menu:
        print(i,menu[i])
    n =  int(input('nhập lựa chọn của bạn ở đây : '))
    if n in menu:
        print(menu[n])
        break
    else:
        print('vui lòng nhập chọn trong menu ')