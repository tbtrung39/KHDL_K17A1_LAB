num=int(input("Nhập số có 3 chữ số: "))
hang_tram=(num//100)%10
hang_chuc=(num//10)%10
hang_don_vi=num%10
print(f'Số vừa nhập có cách đọc là: ',end=' ')
if hang_tram>99:
    if hang_tram==1:
        print('Một trăm', end=' ')
    elif hang_tram==2:
        print('Hai trăm', end=' ')
    elif hang_tram==3:
        print('Ba trăm', end=' ')
    elif hang_tram==4:
        print('Bốn trăm', end=' ')
    elif hang_tram==5:
        print('Năm trăm', end=' ')
    elif hang_tram==6:
        print('Sáu trăm', end=' ')
    elif hang_tram==7:
        print('Bảy trăm', end=' ')
    elif hang_tram==8: 
        print('Tám trăm', end=' ')
    else:
        print('Chín trăm', end=' ')
if hang_chuc==hang_don_vi==0:           
    print('')
if hang_chuc==1:
    print('mười',end=' ')
if hang_chuc==0 and hang_don_vi!=0:     
    print('linh',end=' ')
if hang_chuc==2:
    print('hai mươi', end=' ')
elif hang_chuc==3:
    print('ba mươi', end=' ')
elif hang_chuc==4:
    print('bốn mươi', end=' ')
elif hang_chuc==5: 
    print('năm mươi', end=' ')
elif hang_chuc==6:
    print('sáu mươi', end=' ')
elif hang_chuc==7:
    print('bảy mươi', end=' ')
elif hang_chuc==8:
    print('tám mươi', end=' ')
elif hang_chuc==9:
    print('chín mươi', end=' ')   
if hang_don_vi==1 and hang_chuc==0 and hang_chuc==1:     
    print('một')
if hang_don_vi==1 and hang_chuc>1:     
    print('mốt')
elif hang_don_vi==2:
    print('hai')
elif hang_don_vi==3:
    print('ba')
elif hang_don_vi==4:
    print('bốn')
elif hang_don_vi==5:
    print('lăm')
elif hang_don_vi==6:
    print('sáu')
elif hang_don_vi==7:
    print('bảy')
elif hang_don_vi==8:
    print('tám')
elif hang_don_vi==9:
    print('chín')